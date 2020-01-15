# read big txt file info dataframe
import pandas as pd
import re


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
# print_lines(lines)


# сортировать стрички в 3 разныл листа
import re
print()
print(lines[2])

# split lines
splited_lines = []
for string in lines:
    splited_lines.append(string.split())

# print()
# for i in splited_lines[:3]:
#     print(i)


# print(type(splited_lines))


list_for_texts = lines.copy()
list_for_ids = splited_lines.copy()

# первые два элемента
def get_ids(list):
    ids = []
    count = 0
    for i in list_for_ids:
        ids.insert(count, list_for_ids[count][:2])
        count += 1
    return ids





# в ноы список записать то что русские буквы

def get_texts(list_for_texts):
    texts = []
    for i in list_for_texts:
        texts.append(re.sub("[^а-яА-Я]+", ' ', i))
    return texts

ids = get_ids(list_for_ids)
texts = get_texts(list_for_texts)

print(ids[2])
print(texts[2])
# test



def main():
    get_lines(file_name)
    get_ids(list_for_ids)
    get_texts(list_for_texts)

