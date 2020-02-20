import pandas as pd
from time import time
import files.file_names as f

def drop_duplicate_line(df, new_col_name):
    df.reset_index(drop=True, inplace=True)
    df = df.sort_values("id")
    index = 0
    while index < df.shape[0]-1:
        if df.loc[index, "id"] == df.loc[index + 1, "id"]:
            df.loc[index, new_col_name] = df.loc[index + 1, "text"]
            df = df.drop(index + 1)
            index += 1
        index += 1
    return df

def get_unduplicated_lines():
    df = pd.read_csv(f.id_and_text_fn, index_col=0)
    tos = time()
    i = 1
    while (df["id"].duplicated().sum() > 0):
        tosi = time()
        print(" step ", i)
        print("  rows: ", df.shape[0])
        print("  duplicated: ", df["id"].duplicated().sum())
        df = drop_duplicate_line(df, "t" + i.__str__())
        print("  duplicates left: ", df["id"].duplicated().sum())
        print("time for step ", i, " ", time() - tosi)
        i += 1
        if i % 1000 == 0 :
            print (i)
    print("total time for duplicates ", time() - tos)
    return df