import os
import openpyxl

wb = openpyxl.Workbook()

sheet = wb.get_sheet_by_name("Sheet")
sheet["A1"].value = 42
sheet["A2"] = 'Hello'

sheet2 = wb.create_sheet()
sheet2.title = "My new sheet name"

wb.save("example2.xlsx")
os.system("pause")