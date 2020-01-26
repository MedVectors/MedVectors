import pandas as pd

import read_txt as txt
import read_xls as xls
import solve_duplicates as dp

pd.set_option('display.max_columns', 30)


def concatenate_dataframes(df1, df2):
    df_result = pd.concat([df1, df2], axis=1, sort=True)
    return df_result


df_xls = xls.get_dataframe_from_xls()
df_xls = df_xls.set_index(df_xls.iloc[:, 51].values)
df_texts = txt.get_dataframe_from_txt()
df_texts = dp.get_unduplicated_lines(df_texts)
df_texts = df_texts.set_index(df_texts.loc[:, "id"].values)
print(df_texts)

df_result = concatenate_dataframes(df_xls, df_texts)
print(df_result)

result_file_name = "C:/Users/admin/Downloads/Telegram Desktop/result_no_duplicates.csv"
df_result.to_csv(result_file_name)
