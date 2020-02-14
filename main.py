# concatenate two files
# 4d and 5th steps
import pandas as pd
import mylib as my
from time import time

pd.set_option('display.max_columns', 300)


print(my.get_lines(my.txt_file_name))
ttos = time()


print("1. read xls...")
df_xls = my.get_dataframe_from_xls()
 # use column 51 as indexes
df_xls = df_xls.dropna(subset=["Апгар1"])
df_xls = df_xls.set_index(df_xls.iloc[:, 51].values)
print(" done")
print("df xls size: " + str(df_xls.shape))
# print(df_xls)

print("2. read txt...")
df_texts = my.get_dataframe_from_txt()
print(" done")
print("df txt size: " + str(df_texts.shape))

print("solve duplicates in txt...")
df_texts = my.get_unduplicated_lines(df_texts)
print("duplicates solved!")
df_texts = df_texts.set_index(df_texts.loc[:, "id"].values) # use column id as indexes
print("\ndf txt without duplicates size: " + str(df_texts.shape))


print("concatenate dataframes...")
concatenated_df = my.concatenate_dataframes(df_xls, df_texts)
print(" done")

concatenated_df = concatenated_df.dropna(subset=["Апгар1"])

print("\nconcatenated dataframe size: " + str(concatenated_df.shape))
print(concatenated_df["Апгар1"])

print("save to file...")
my.save_dataframe_to_file(concatenated_df, my.concatenated_dataframe_file_name)
print("saved to " + my.concatenated_dataframe_file_name)

print("geting data with apgar values")
only_apgar_dataset = my.get_specific_column_dataset(my.concatenated_dataframe_file_name, "Апгар1")
my.save_dataframe_to_file(only_apgar_dataset, my.apgar_file_name)
print("new dataset with apgar values saved to file " + my.apgar_file_name)
print("\nonly apgar dataframe size: " + str(only_apgar_dataset.shape))

print("apgar dataset",only_apgar_dataset.shape)

print("leaving only relevant columns")
short_df = my.leave_only_relevant_columns(my.apgar_file_name) # columns with highest correlation
print("save to file " + my.relevant_columns_file_name)
my.save_dataframe_to_file(short_df, my.relevant_columns_file_name)
print(" done")
print("\nshort dataframe size: " + str(short_df.shape))

print("prepere text for prediciton... ")
text_df = my.put_text_in_one_colunm(my.relevant_columns_file_name)
print(" done")
print("\ntext-in-one-column dataframe size: " + str(text_df.shape))

my.save_dataframe_to_file(text_df, my.cleaned_text_file_name)
print("save to file " + my.cleaned_text_file_name)

# drop nan text
df = my.get_text_df(my.cleaned_text_file_name)

# print("DF: ", df)
my.save_dataframe_to_file(df, my.cleaned2)
print("\ncleaned 2 dataset shape: " + str(df.shape))

my_corpora = my.gather_corpora_from_file(my.cleaned2)
print("compile corpora... done")

print("size of corpora", my_corpora.__sizeof__())

print("train w2v_model model... ")
w2v_model = my.get_word2vec_model(my_corpora)
print(" done")

print("START ADDING VECTORS")
df_with_vectors = my.add_vectors_to_dataframe(my.cleaned2, w2v_model)
print("adding vectors ... done")
print("\nwith vectors dataframe size: " + str(df_with_vectors.shape))

my.save_dataframe_to_file(df_with_vectors, my.result_file_name)
print("dataset with vectors has been saved to file")

print("predict apgar using only numbers")
my.predict_without_text(my.result_file_name)
my.predict_with_text(my.result_file_name)

ttof = time()
print("TOTAL TIME ",  ttof - ttos)















