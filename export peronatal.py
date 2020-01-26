# считывает файл

import pandas as pd
from pandas import read_excel

file_name = "C:/Users/admin/Downloads/Telegram Desktop/perinatal.xlsx"


def load_dataframe_from_file(filename):
    # load the file
    xl_file = pd.ExcelFile(filename)
    # print sheets
    sheet_name = xl_file.sheet_names[0]
    # load sheet to data frame
    data_frame = xl_file.parse(sheet_name)
    return data_frame


my_data_frame = load_dataframe_from_file(file_name)
