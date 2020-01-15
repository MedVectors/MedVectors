import pandas as pd

import read_txt as txt
import read_xls as xls

pd.set_option('display.max_columns', 30)

df_xls = xls.get_dataframe_from_xls()
df_xls = df_xls.set_index(df_xls.iloc[:,51].values)
# print(df_xls)

def concatenate_dataframes(df1, df2):
    df_result = pd.concat([df1, df2], axis=1, sort=True)
    return df_result


df_texts = txt.get_dataframe_from_txt()
df_texts = df_texts.set_index(df_texts.iloc[:,0].values)
# print(df_texts)
df_texts = df_texts.drop_duplicates(subset='id', keep='last')
# print(df_texts)

df_result = concatinate_dataframes(df_xls, df_texts)
print(df_result)


result_file_name = "C:/Users/admin/Downloads/Telegram Desktop/result_no_duplicates.xlsx"
df_result.to_csv(result_file_name)

# не устанавливать ид, а попробовать записать повторяюзиеся в разные новые столбцы,
# а потом устновить ид и сконкатенировать

# duplicated_ids = df_texts.index.get_duplicates()
# print(duplicated_ids)