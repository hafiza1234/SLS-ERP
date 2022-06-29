from openpyxl import load_workbook
wb = load_workbook("Py_data.xlsx")
sheet = wb.worksheets[0]
a1 = sheet['A1'].value
b2 = sheet['B2'].value
c3 = sheet['C3'].value
print(a1,b2,c3)