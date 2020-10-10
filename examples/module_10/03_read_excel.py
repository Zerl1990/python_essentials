import openpyxl
import os


script_dir = os.path.dirname(__file__)
script_dir = os.path.abspath(script_dir)
abs_file_path = os.path.join(script_dir, 'example.xlsx')


try:
    workbook = openpyxl.load_workbook(abs_file_path)
    worksheet = workbook['example2']
    for row in worksheet.iter_rows(min_row=2):
        cell_values = []
        for cell in row:
            cell_values.append(str(cell.value))
        print(', '.join(cell_values))
except:
    print('Verifica si el archivo existe, y si la hoja es valida')
