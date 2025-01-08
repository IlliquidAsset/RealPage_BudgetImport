# Budget Processor Tool

This tool automates the process of monitoring a folder for new Excel files, extracting budget data from the "Owner Budget Report" (OBR) sheet, and appending the processed data to a master CSV file.

## Prerequisites
1. **Python Installation**:
   - Ensure Python 3.8 or higher is installed on your computer.
   - Download Python from [python.org](https://www.python.org/).
   - During installation, check the box to "Add Python to PATH."

2. **Required Python Libraries**:
   - Install the following libraries using pip:
     ```bash
     pip install pandas openpyxl watchdog
     ```

3. **File Structure**:
   - Create the following folder structure:
     ```
     Project Root
     ├── zappy
     │   └── zappy.py  # Ensure the zappy.py file is saved here.
     ├── Budgets to RP
     │   ├── watch     # Folder where new Excel files will be placed.
     │   ├── output    # Folder where the master file (BUDGETS.csv) will be saved.
     │   └── BUDGETS.csv  # The initial master file (optional).
     ```

4. **Source Files**:
   - Ensure new Excel files placed in the `watch` folder have a sheet named "Owner Budget Report" and named ranges `EID` and `Name`.

---

## Setting Up the Tool
1. **Download the Script**:
   - Save the provided Python script (Budget Processor Tool) in the `Project Root` folder.

2. **Modify Configuration**:
   - Open the script in a text editor.
   - Update the following paths to match your file structure:
     ```python
     watch_dir = r"C:\Users\volprop\Desktop\Project Root\Budgets to RP\watch"
     output_file = r"C:\Users\volprop\Desktop\Project Root\Budgets to RP\output\BUDGETS.csv"
     ```

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the `Project Root` folder:
     ```bash
     cd "C:\Users\volprop\Desktop\Project Root"
     ```
   - Run the script:
     ```bash
     python budget_processor.py
     ```

---

## Using the Tool
1. **Start Monitoring**:
   - Once the script is running, it will monitor the `watch` folder for new files.
   - Any valid Excel files placed in the folder will be processed automatically.

2. **Processing Logic**:
   - For each new file in the `watch` folder:
     - Extract the `EID` and `Name` named ranges to form the `Location_ID` in the format `EID--Name`.
     - Identify columns labeled "Month Ended ..." to extract monthly financial data.
     - Append the data to the `BUDGETS.csv` file in the `output` folder.

3. **Output File**:
   - The processed data is saved in `BUDGETS.csv` with the following columns:
     - `RealPage Account`
     - `Location_ID`
     - `Month Ended` (in `YYYY/MM/DD` format)
     - `Amount`

---

## Error Handling
1. **Debugging Logs**:
   - The tool uses the `zappy` debugging module to log errors and track versions.
   - Logs are saved in `zappy/debug_log.json`.

2. **Common Issues**:
   - **Missing Named Ranges**:
     - Ensure the Excel files have the named ranges `EID` and `Name`.
     - If these ranges are missing, the file will be skipped.
   - **Invalid Column Names**:
     - Ensure the sheet "Owner Budget Report" contains columns labeled "Month Ended ..." for monthly data.

---

## Stopping the Tool
1. To stop the script, press `Ctrl + C` in the terminal.
2. Close the terminal to terminate the monitoring process.

---

## FAQ
### What happens if a file is processed twice?
Duplicate records are automatically skipped during the appending process, so no duplicates will be added to `BUDGETS.csv`.

### Can I use this tool for historical data?
Yes. Place older Excel files in the `watch` folder, and the tool will process them as usual.

### How can I verify the processed data?
Open the `BUDGETS.csv` file in any text editor or spreadsheet software to review the appended data.

---

## Support
For further assistance, contact your technical team or refer to the debugging logs in `zappy/debug_log.json`.

#   R e a l P a g e _ B u d g e t I m p o r t  
 