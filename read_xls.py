import xlrd
import pandas as pd

file_name = "C:/Users/admin/Downloads/Telegram Desktop/perinatal.xlsx"
sheet_name = "L1"

def get_sheet_from_xls(file_name):
    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_index(0)
    return sheet

def get_dataframe_from_xls():
    return pd.read_excel(file_name, sheet_name)

def get_dead_indexes(sheet):
    dead = []
    for i in range(sheet.nrows):
        if sheet.cell_value(i, 23) != "":
            print(i, sheet.cell_value(i, 23))
            dead.append(i)
    return dead

def print_sheet_information(sheet):
    print("Строк всего " + sheet.nrows.__str__())
    print("Столбцов всего " + sheet.ncols.__str__())

    print("НАЗВАНИЯ СТОЛБЦОВ")
    for i in range(sheet.ncols):
        print(i, sheet.cell_value(0, i))

    print("Содержимое строки 1")
    print(sheet.row_values(0))

    print("строки где смерть")
    for i in get_dead_indexes(sheet):
        print(sheet.row_values(i))


def run():
     sheet = get_sheet_from_xls(file_name)

     print(sheet)

     print(type(sheet))




