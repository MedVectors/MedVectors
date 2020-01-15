from numba import jit, cuda
import numba
import read_txt as txt
import pandas as pd
pd.set_option('display.max_columns', 30)

@numba.jit
def run(df, number_of_iterations, col_name):
    index = 0
    while index < number_of_iterations:
        if df.loc[index, "id"] == df.loc[index + 1, "id"]:
            df.loc[index, col_name] = df.loc[index + 1, "text"]
            df = df.drop(index + 1)
            index += 1
        index += 1
    return df

def get_unduplicated_lines(df):
    print("rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.sort_values("id")
    df = run(df, df.shape[0] - 1, "t1")
    print("duplicated: " + df["id"].duplicated().sum().__str__())

    print("rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.drop("level_0", 1)
    df = df.sort_values("id")
    df = run(df, df.shape[0] - 1, "t2")
    print("duplicated: " + df["id"].duplicated().sum().__str__())

    print("rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.drop("level_0", 1)
    df = df.sort_values("id")
    df = run(df, df.shape[0] - 1, "t3")
    print("duplicated: " + df["id"].duplicated().sum().__str__())

    print("rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.drop("level_0", 1)
    df = df.sort_values("id")
    df = run(df, df.shape[0] - 1, "t4")
    print("duplicated: " + df["id"].duplicated().sum().__str__())

    print("rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.drop("level_0", 1)
    df = df.sort_values("id")
    df = run(df, df.shape[0] - 1, "t5")
    print("duplicated: " + df["id"].duplicated().sum().__str__())

    print("rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.drop("level_0", 1)
    df = df.sort_values("id")
    df = run(df, df.shape[0] - 1, "t6")
    print("duplicated: " + df["id"].duplicated().sum().__str__())

    return df

