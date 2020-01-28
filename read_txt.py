# read big txt file info dataframe (library)
# 1st step
import pandas as pd
import re

file_name = "C:/Users/admin/Downloads/Telegram Desktop/ana.txt"
utf8 = "utf8"


def get_lines(filename):
    text = []
    with open(filename, "rb") as f:
        line = f.readline().decode(utf8)
        counter = 1
        while line:
            text.insert(counter, line.strip())
            line = f.readline().decode(utf8)
            counter += 1
    return text


def print_lines(lines):
    for i in lines:
        print(i)


def split_lines(lines):
    splited_lines = []
    for string in lines:
        splited_lines.append(string.split())
    return splited_lines


def get_ids(list_for_ids):
    ids = []
    index = 0
    for i in list_for_ids:
        ids.insert(index, list_for_ids[index][0])
        index += 1
    return ids


def get_texts(list_for_texts):
    texts = []
    for i in list_for_texts:
        texts.append(re.sub("[^а-яА-Я]+", ' ', i))
    return texts


def combine_ids_and_texts(ids, texts):
    ids_and_texts = []
    index = 0
    for line in ids:
        ids_and_texts.insert(index, ("'" + ids[index].__str__() + "' , '" + texts[index].__str__() + "'"))
        index += 1
    return ids_and_texts


def get_list_of_ids_and_texts():
    list_for_texts = get_lines(file_name).copy()
    list_for_ids = split_lines(list_for_texts.copy()).copy()
    ids_and_text = combine_ids_and_texts(get_ids(list_for_ids), get_texts(list_for_texts))
    return ids_and_text


def get_dataframe_from_txt():
    ids = get_ids(split_lines(get_lines(file_name)))
    texts = get_texts(get_lines(file_name))
    df = pd.DataFrame(list(zip(ids, texts)), columns=["id", "text"])
    return df
