import datetime
import openpyxl
from openpyxl.worksheet.table import Table, TableStyleInfo

from tester import infofill

def excel_tableprint(infofill):
    # Step 1: Set the sheet name based on the current date
    shtname = str(datetime.date.today())

    # Step 2: Load the Excel file
    wb = openpyxl.load_workbook('hello.xlsx')

    # Step 3: Get the active sheet
    ws = wb.active

    # Step 4: Append the table headers to the sheet
    ws.append(["Entry No.", "Flat No.", "CustomerID", "Date", "Amount"])

    # Step 5: Append the data from infofill to the sheet
    for column in infofill:
        ws.append(column)

    # Step 6: Create a table and apply formatting
    tab = Table(displayName="Table1", ref="A1:E5")
    style = TableStyleInfo(
        name="TableStyleMedium9",
        showFirstColumn=False,
        showLastColumn=False,
        showRowStripes=True,
        showColumnStripes=True
    )
    tab.tableStyleInfo = style
    ws.add_table(tab)

    # Step 7: Save the modified Excel file
    wb.save('hello.xlsx')

if __name__ == '__main__':
    excel_tableprint(infofill)
