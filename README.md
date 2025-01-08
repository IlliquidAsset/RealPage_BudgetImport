# Budget Processor Tool: README

This document provides detailed instructions on setting up and using the Budget Processor Tool. Designed for automation, this tool streamlines the process of monitoring a folder for new Excel files, extracting budget data from the "Owner Budget Report" (OBR) sheet, and appending the processed data to a master CSV file.

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
   - Create the following folder structure in the root directory where the script will run:
     ```plaintext
     Project Root
     ├── zappy
     │   └── zappy.py  # Ensure the zappy.py file is saved here.
     ├── Budgets to RP
     │   ├── watch     # Folder where new Excel files will be placed.
     │   ├── output    # Folder where the master file (BUDGETS.csv) will be saved.
     │   └── BUDGETS.csv  # The initial master file (optional).
     ```

4. **Source Files**:
   - Ensure new Excel files placed in the `watch` folder meet these requirements:
     - Contain a sheet named "Owner Budget Report."
     - Include named ranges `EID` and `Name` for identifying the location.

---

## Setting Up the Tool

1. **Download the Script**:
   - Save the provided Python script (Budget Processor Tool) in the `Project Root` folder.

2. **No Configuration Required**:
   - The script uses relative paths, ensuring it works out of the box as long as the folder structure is adhered to.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the `Project Root` folder:
     ```bash
     cd "Project Root"
     ```
   - Start the script:
     ```bash
     python budget_processor.py
     ```

---

## Using the Tool

1. **Monitoring Process**:
   - Once the script is running, it will continuously monitor the `watch` folder for new Excel files.
   - Upon detecting a new file, it processes the data automatically.

2. **Data Processing Steps**:
   - For each new file, the script:
     - Extracts the `EID` and `Name` from the named ranges to construct `Location_ID` in the format `EID--Name`.
     - Identifies and extracts monthly financial data from columns labeled "Month Ended ...".
     - Appends the data to the `BUDGETS.csv` file in the `output` folder.

3. **Output Format**:
   - The resulting `BUDGETS.csv` file will contain:
     - `RealPage Account`
     - `Location_ID`
     - `Month Ended` (formatted as `YYYY/MM/DD`)
     - `Amount`

---

## Error Handling

1. **Debugging Logs**:
   - Errors and process tracking information are logged using the `zappy` module.
   - Debug logs are saved in `zappy/debug_log.json`.

2. **Common Issues**:
   - **Missing Named Ranges**:
     - Ensure the Excel files include the named ranges `EID` and `Name`.
     - If these ranges are absent, the file will be skipped with an error logged.
   - **Invalid Column Names**:
     - Ensure the "Owner Budget Report" sheet contains columns labeled "Month Ended ..." for monthly data.

---

## Stopping the Tool

1. To stop the script, press `Ctrl + C` in the terminal.
2. Close the terminal to terminate the monitoring process entirely.

---

## FAQ

### What happens if a file is processed twice?

The script automatically skips duplicate records during the appending process, ensuring no duplicates in `BUDGETS.csv`.

### Can I use this tool for historical data?

Yes. Place older Excel files in the `watch` folder, and the script will process them as usual.

### How can I verify the processed data?

Open the `BUDGETS.csv` file in any text editor or spreadsheet software to review the appended data.

---

## Support

For further assistance, contact your technical team or refer to the debugging logs in `zappy/debug_log.json`. This log provides detailed insights into processing events and errors, enabling quick troubleshooting.

