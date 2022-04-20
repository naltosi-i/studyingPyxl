import openpyxl
import pathlib

file_path = 'studyingPyxlBook1.xlsx'

wb = openpyxl.load_workbook('studyingPyxlBook1.xlsx') # Excelファイルを読み込むメソッド
# pathlib.Path('test').mkdir(exist_ok=True)
# wb.save('test/studyingPyxlBook3.xlsx') # 変数に格納されたExcelファイルを保存するメソッド

ws = wb.worksheets[0]

c1 = ws['A1']
c2 = ws['A2']
c3 = ws['A3']
c4 = ws['A4']

c1.value = 'test'
c2.value = 'Hello world.'
c3.value = 101
c4.value = '101'

wb.save(file_path)