import os
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name("Sheet")
sheet["A1"].value = 42
sheet["A2"] = 'Hello'
wb.save('createdworkbook.xlsx')

os.system("pause")