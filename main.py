import pandas as pd
from lib import mylib as my
import lib.txt_to_csv as txt
from files import file_names as f
from lib import prediction as p
from lib import xls_to_csv as xls
from time import time
import re
import lib.duplicates as d

pd.set_option('display.max_columns', 300)


# print(my.get_lines_as_one_line(f.txt_file_name))
ttos = time()

# tos1 = time()
# print("1. read xls...")
# xls.read_xls()
# print(" done, time:", time()-tos1)

# tos2 = time()
# print("2. read txt...")
# txt.read_txt_to_csv()
# print(" done, time:", time()-tos2)


# tos3 = time()
# print("3. solve duplicates in txt...")
# df_texts = d.get_unduplicated_lines()
# print(" duplicates solved!")
# df_texts = df_texts.set_index(df_texts.loc[:, "id"].values) # use column id as indexes
# my.save_dataframe_to_file(df_texts, f.no_dupicates_fn)
# print("\ndf txt without duplicates size: " + str(df_texts.shape))
# print(" time:", time()-tos3)


# tos4 = time()
# print("4. concatenate dataframes...")
# df_xls = pd.read_csv(f.xls_to_csv_fn, index_col=0)
# df_texts = pd.read_csv(f.no_dupicates_fn, index_col=0)
# concatenated_df = pd.concat([df_xls, df_texts], axis=1, sort=True)
# print(" done")
# print(" concatenated dataframe size: " + str(concatenated_df.shape))
# my.save_dataframe_to_file(concatenated_df, f.concatenated_df_fn)
# print(" time:", time()-tos4)

tos5 = time()
print("5. drop rows without apgar values")
overlap_rows_df = my.leav_only_overlap_rows(f.concatenated_df_fn)
my.save_dataframe_to_file(overlap_rows_df, f.overlap_concatenated_fn)
print(" done")
print(" time:", time()-tos5)

# tos6 = time()
# print("6. preprocess texts")
# only_apgar_dataset = my.preprocess(only_apgar_dataset)
# print(" done")
# print(" apgar dataset size: " ,only_apgar_dataset.shape)
# print(" time:", time()-tos6)

# my.save_dataframe_to_file(only_apgar_dataset, my.apgar_file_name)
# print("new dataset with apgar values saved to file " + my.apgar_file_name)
# print("only apgar dataframe size: " + str(only_apgar_dataset.shape))


# tos7 = time()
# print("7. keep only relevant columns...")
# short_df = my.leave_only_relevant_columns(f.apgar_file_name) # columns with highest correlation
# print("save to file " + f.relevant_columns_file_name)
# my.save_dataframe_to_file(short_df, f.relevant_columns_file_name)
# print(" done")
# print(" short dataframe size: " + str(short_df.shape))
# print(" time:", time()-tos7)


# tos9 = time()
# print("9. compile corpora... ")
# my_corpora = my.gather_corpora_from_file(my.cleaned_text_file_name)
# print(" done")
# print(" size of corpora", my_corpora.__sizeof__())
# print(" time:", time()-tos9)
#
# tos10 = time()
# print("10. train w2v_model model... ")
# w2v_model = my.get_word2vec_model(short_df["text"])
# print(" done")
# print(" time:", time()-tos10)
#
# tos11 = time()
# print("11. START ADDING VECTORS")
# df_with_vectors = my.add_vectors_to_dataframe(f.cleaned_text_file_name, w2v_model)
# print("adding vectors ... done")
# print(" with vectors dataframe size: " + str(df_with_vectors.shape))
# print(" time:", time()-tos11)
#
# my.save_dataframe_to_file(df_with_vectors, f.result_file_name)
# print(" dataset with vectors has been saved to file")
#
# print("predict apgar using only numbers")
# p.predict_without_text(f.result_file_name)
# p.predict_with_text(f.result_file_name)

ttof = time()
print("TOTAL TIME ",  ttof - ttos)















