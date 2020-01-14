# read big txt file info dataframe
import pandas as pd

file_name = "C:/Users/admin/Downloads/Telegram Desktop/ana.txt"
utf8 = "utf8"

def get_lines(filename):
    # лист где каждый элемент это стока из файлв
    text = []
    with open(file_name, "rb") as f:
        line = f.readline().decode(utf8)
        counter = 1
        while line:
            text.insert(counter, line.strip())
            line = f.readline().decode(utf8)
            counter += 1
    return text

def print_lines(list):
    for i in list:
        print(i)


lines = get_lines(file_name)
print_lines(lines)


