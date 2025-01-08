import os
import pandas as pd
from openpyxl import load_workbook
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from zappy import run_with_debug  # Import zappy integration

class BudgetFileHandler(FileSystemEventHandler):
    def __init__(self, watch_dir, output_file):
        self.watch_dir = watch_dir
        self.output_file = output_file

    def get_named_range_values(self, file_path, range_name):
        """Extract a named range value from an Excel file."""
        wb = load_workbook(file_path, data_only=True)
        try:
            named_range = wb.defined_names[range_name]
            destination = named_range.attr_text.split("!")[1]
            sheet_name, cell = destination.split("!")
            value = wb[sheet_name.strip()][cell.strip()].value
            return value
        except Exception as e:
            raise ValueError(f"Error reading named range '{range_name}': {e}")
        finally:
            wb.close()

    def process_file(self, file_path):
        print(f"Processing: {file_path}")
        
        # Load the Owner Budget Report sheet
        try:
            data = pd.read_excel(file_path, sheet_name="Owner Budget Report", skiprows=2)
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return

        # Extract EID and Name from named ranges
        try:
            eid = self.get_named_range_values(file_path, "EID")
            name = self.get_named_range_values(file_path, "Name")
            location_id = f"{eid}--{name}"
        except Exception as e:
            print(f"Error extracting named ranges: {e}")
            return

        # Find all date-related columns by pattern matching "Month Ended"
        date_columns = [col for col in data.columns if "Month Ended" in str(col)]
        if not date_columns:
            print(f"No 'Month Ended' columns found in {file_path}. Skipping.")
            return

        # Map date columns to correct format (e.g., 2025/01/31)
        date_mapping = {
            col: pd.to_datetime(col.split(" ")[-2] + " 2025", format="%B %Y").strftime("%Y/%m/%d")
            for col in date_columns
        }

        # Extract relevant line items from OBR
        relevant_data = data[["RealPage Account"] + date_columns].copy()
        relevant_data["Location_ID"] = location_id
        relevant_data = relevant_data.melt(
            id_vars=["RealPage Account", "Location_ID"],
            value_vars=date_columns,
            var_name="Month Ended",
            value_name="Amount"
        )
        relevant_data["Month Ended"] = relevant_data["Month Ended"].map(date_mapping)
        relevant_data = relevant_data.dropna(subset=["Amount"])

        # Load existing output or create a new one
        if os.path.exists(self.output_file):
            master_data = pd.read_csv(self.output_file)
        else:
            master_data = pd.DataFrame(columns=["RealPage Account", "Location_ID", "Month Ended", "Amount"])

        # Append only new records
        updated_master = pd.concat([master_data, relevant_data]).drop_duplicates()

        # Write back to the output file
        updated_master.to_csv(self.output_file, index=False)
        print(f"Updated master file: {self.output_file}")

    def on_created(self, event):
        if event.is_directory or not event.src_path.endswith((".xlsm", ".xlsx")):
            return
        self.process_file(event.src_path)

def watch_folder():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    watch_dir = os.path.join(base_dir, "Budgets to RP", "watch")
    output_file = os.path.join(base_dir, "Budgets to RP", "output", "BUDGETS.csv")

    def app_logic():
        event_handler = BudgetFileHandler(watch_dir, output_file)
        observer = Observer()
        observer.schedule(event_handler, path=watch_dir, recursive=False)
        observer.start()
        try:
            print(f"Watching folder: {watch_dir}")
            while True:
                pass
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

    # Run the folder watcher logic wrapped with Zappy's debug support
    run_with_debug("Budget File Processor", app_logic)

if __name__ == "__main__":
    watch_folder()
