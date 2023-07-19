# India_GEB_Bulk_Bill_pending
Program is developed for Scrapping Bulk Bill id form GEB(Gujarat electricity board) for amount to be paid
# DGVCL Bill Scraper

This script automates the process of retrieving bill information from the DGVCL (Dakshin Gujarat Vij Company Ltd) website using Selenium and Python.

## Usage

1. Install the required packages listed in the `requirements.txt` file.
2. Update the `signup_url` variable with the correct URL of the DGVCL website.
3. Add the customer numbers for which you want to retrieve bill details to the `coustomer_number` list.
4. Run the `Dgvcl` function by executing the script.

```bash
python script.py

    The script will open a headless Firefox browser, navigate to the DGVCL website, and retrieve the bill information for each customer number provided.
    The bill details will be stored in the infofill list.
    You can modify the script to save the bill details to an Excel file or perform any other desired actions with the data.

Feel free to customize the script as per your requirements and contribute to the project by submitting pull requests.


Please make sure to install the required packages listed in the `requirements.txt` file before running the script.
