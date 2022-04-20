import openpyxl
import pathlib

wb = openpyxl.load_workbook('studyingPyxlBook1.xlsx') # Excelファイルを読み込むメソッド
pathlib.Path('test').mkdir(exist_ok=True)
wb.save('test/studyingPyxlBook3.xlsx') # 変数に格納されたExcelファイルを保存するメソッド



