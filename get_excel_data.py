from openpyxl import load_workbook

wb = load_workbook('C:/workspace/GitHub/RPA_Crawling/data.xlsx') # excel file path
data = wb.active

print(data['A1'].value) # get A1 data