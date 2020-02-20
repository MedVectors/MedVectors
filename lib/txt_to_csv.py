import re
import pandas as pd
import files.file_names as f
import lib.mylib as my


def get_ids_and_texts(filename):
    lines = []
    with open(filename, "rb") as f:
        line = f.readline().decode('utf8')
        counter = 1
        while line:
            lines.insert(counter, line.strip().split())
            line = f.readline().decode('utf8')
            counter += 1

    ids, texts = [], []
    index = 0
    for line in lines:
        ids.insert(index, line[0])
        texts.insert(index, re.sub("[^а-яА-Я]+", ' ', str(line)))
        index += 1
    return ids, texts


def read_txt_to_csv():
    ids, texts = get_ids_and_texts(f.txt_file_name)
    df_texts = pd.DataFrame(list(zip(ids, texts)), columns=["id", "text"])
    my.save_dataframe_to_file(df_texts, f.id_and_text_fn)