import pandas as pd
import mylib as my
from time import time

pd.set_option('display.max_columns', 300)


# print(my.get_lines(my.txt_file_name))
ttos = time()

tos1 = time()
print("1. read xls...")
df_xls = my.get_dataframe_from_xls()
df_xls = df_xls.dropna(subset=["Апгар1"])
df_xls = df_xls.set_index(df_xls.loc[:, "m_id"].values)
print(" done")
print(" df xls size: " + str(df_xls.shape))
print(" time:", time()-tos1)
# print(df_xls)

tos2 = time()
print("2. read txt...")
df_texts = my.get_dataframe_from_txt()
print(" done")
print(" df txt size: " + str(df_texts.shape))
print(" time:", time()-tos2)

tos3 = time()
print("3. solve duplicates in txt...")
df_texts = my.get_unduplicated_lines(df_texts)
print(" duplicates solved!")
df_texts = df_texts.set_index(df_texts.loc[:, "id"].values) # use column id as indexes
print("\ndf txt without duplicates size: " + str(df_texts.shape))
print(" time:", time()-tos3)

tos4 = time()
print("4. concatenate dataframes...")
concatenated_df = my.concatenate_dataframes(df_xls, df_texts)
print(" done")
print(" concatenated dataframe size: " + str(concatenated_df.shape))
print(" time:", time()-tos4)

print("save to file...")
my.save_dataframe_to_file(concatenated_df, my.concatenated_dataframe_file_name)
print("saved to " + my.concatenated_dataframe_file_name)

tos5 = time()
print("5. drop rows without apgar values")
only_apgar_dataset = my.get_specific_column_dataset(my.concatenated_dataframe_file_name, "Апгар1")
print(" done")
print(" time:", time()-tos5)

tos6 = time()
print("6. preprocess texts")
only_apgar_dataset = my.preprocess(only_apgar_dataset)
print(" done")
print(" apgar dataset size: " ,only_apgar_dataset.shape)
print(" time:", time()-tos6)


my.save_dataframe_to_file(only_apgar_dataset, my.apgar_file_name)
print("new dataset with apgar values saved to file " + my.apgar_file_name)
print("\nonly apgar dataframe size: " + str(only_apgar_dataset.shape))

tos7 = time()
print("7. keep only relevant columns...")
short_df = my.leave_only_relevant_columns(my.apgar_file_name) # columns with highest correlation
print("save to file " + my.relevant_columns_file_name)
my.save_dataframe_to_file(short_df, my.relevant_columns_file_name)
print(" done")
print(" short dataframe size: " + str(short_df.shape))
print(" time:", time()-tos7)

tos8 = time()
print("8. put text in one column... ")
text_df = my.put_text_in_one_colunm(my.relevant_columns_file_name)
print(" done")
print(" text-in-one-column dataframe size: " + str(text_df.shape))
print(" time:", time()-tos8)

my.save_dataframe_to_file(text_df, my.cleaned_text_file_name)
print(" save to file " + my.cleaned_text_file_name)

tos9 = time()
print("9. compile corpora... ")
my_corpora = my.gather_corpora_from_file(my.cleaned_text_file_name)
print(" done")
print(" size of corpora", my_corpora.__sizeof__())
print(" time:", time()-tos9)

tos10 = time()
print("10. train w2v_model model... ")
w2v_model = my.get_word2vec_model(my_corpora)
print(" done")
print(" time:", time()-tos10)

tos11 = time()
print("11. START ADDING VECTORS")
df_with_vectors = my.add_vectors_to_dataframe(my.cleaned_text_file_name, w2v_model)
print("adding vectors ... done")
print(" with vectors dataframe size: " + str(df_with_vectors.shape))
print(" time:", time()-tos11)

my.save_dataframe_to_file(df_with_vectors, my.result_file_name)
print(" dataset with vectors has been saved to file")

# print("predict apgar using only numbers")
# my.predict_without_text(my.result_file_name)
# my.predict_with_text(my.result_file_name)

ttof = time()
print("TOTAL TIME ",  ttof - ttos)















