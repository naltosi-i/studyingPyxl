import openpyxl

wb = openpyxl.load_workbook('studyingPyxlBook1.xlsx')
print(wb.sheetnames)