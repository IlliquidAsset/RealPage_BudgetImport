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

3. **Git Installation**:
   - Install Git if it is not already installed on your system.
   - Download Git from [git-scm.com](https://git-scm.com/) and follow the installation instructions for your operating system.

---

## Setting Up the Tool

1. **Clone the Repository**:
   - Open a terminal or command prompt and navigate to the directory where you want to set up the project.
   - Run the following command to clone the repository:
     ```bash
     git clone https://github.com/IlliquidAsset/RealPage_BudgetImport.git
     ```

2. **Navigate to the Project Directory**:
   - Change into the project directory:
     ```bash
     cd RealPage_BudgetImport
     ```

3. **Install Dependencies**:
   - Ensure the required Python libraries are installed by running:
     ```bash
     pip install pandas openpyxl watchdog
     ```

4. **Run the Script**:
   - Start the script by running:
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

