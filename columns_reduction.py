import pandas as pd

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)

file_name = "apgar2.csv"
df = pd.read_csv(file_name)

def drop_columns(dataframe):
    dataframe = dataframe.drop('t4', 1)
    dataframe = dataframe.drop('t5', 1)
    dataframe = dataframe.drop('t6', 1)
    return dataframe

def convert_types(dataframe):
    dataframe["Резус_ребенок"] = dataframe["Резус_ребенок"].astype(str)
    dataframe["text"] = dataframe["text"].astype(str)
    dataframe["t1"] = dataframe["t1"].astype(str)
    dataframe["t2"] = dataframe["t2"].astype(str)
    dataframe["t3"] = dataframe["t3"].astype(str)
    return dataframe

def replace_nan_in_column(dataframe, column_name):
    for i in range(dataframe.shape[0]):
        cur = dataframe.loc[i, column_name]
        if (cur == "nan"):
            dataframe.loc[i, column_name] = ""
    return dataframe

def drop_wrong_rows(dataframe):
    for i in range(dataframe.shape[0]):
        cur = dataframe.loc[i, "Резус_ребенок"]
        # print(cur)
        if cur != "RhPlus" and cur != "RhMin" and cur != "nan":
            print(cur)
    return dataframe

def replace_nun(dataframe):
    dataframe = replace_nan_in_column(dataframe, "text")
    dataframe = replace_nan_in_column(dataframe, "t1")
    dataframe = replace_nan_in_column(dataframe, "t2")
    dataframe = replace_nan_in_column(dataframe, "t3")
    return  dataframe

def reorder_and_drop(df):
    # rename
    df = df.rename(columns={'Апгар1': 'target'})
    df = df.rename(columns={"Unnamed: 0.1": 'id_2'})
    df = df.rename(columns={"text": 'text_1'})
    df = df.rename(columns={"t1": 'text_2'})
    df = df.rename(columns={"t2": 'text_3'})
    df = df.rename(columns={"t3": 'text_4'})

    # change order
    cols = df.columns.to_list()
    cols = cols[38:39] + cols[:38] + cols[39:]
    df = df[cols]

    # drop some
    df = df.drop("Unnamed: 0", axis=1)
    df = df.drop('level_0', axis=1)
    df = df.drop('матьайди', axis=1)
    df = df.drop('id', axis=1)
    df = df.drop('index', axis=1)

    # print
    for column in df.columns:
        print(column)

    return df

df = convert_types(df)
df = drop_columns(df)
df = drop_wrong_rows(df)
df = replace_nun(df)
df = reorder_and_drop(df)

result_file_name = "apgar3.csv"
df.to_csv(result_file_name)

print("saved to file ")


