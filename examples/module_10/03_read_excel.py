import openpyxl
import os


script_dir = os.path.dirname(__file__)
script_dir = os.path.abspath(script_dir)
abs_file_path = os.path.join(script_dir, 'example.xlsx')

workbook = openpyxl.load_workbook(abs_file_path)
worksheet = workbook['example']

for row in worksheet.iter_rows(min_row=2):
    cell_values = []
    for cell in row:
        cell_values.append(str(cell.value))
    print(', '.join(cell_values))
