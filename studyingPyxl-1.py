import imp
import openpyxl
import pathlib

'''
wb = openpyxl.load_workbook('studyingPyxlBook1.xlsx') # Excelファイルを読み込むメソッド
wb.save('studyingPyxlBook2.xlsx') # 変数に格納されたExcelファイルを保存するメソッド
'''

pathlib.Path('test').mkdir(exist_ok=True)
