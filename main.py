import pandas as pd
from gensim.models import Word2Vec

from lib import mylib as my
from files import file_names as f
from lib import correlation as s
from lib import w2v_model as wm

from time import time

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

# tos5 = time()
# print("5. drop rows without apgar values")
# overlap_rows_df = my.leav_only_overlap_rows(f.concatenated_df_fn)
# my.save_dataframe_to_file(overlap_rows_df, f.overlap_concatenated_fn)
# print(" done")
# print(" time:", time()-tos5)

# tos6 = time()
# print("6. preprocess texts")
# df = pp.preproc()
# my.save_dataframe_to_file(df, f.after_text_preprocessing_fn)
# print(" done")
# print(" apgar dataset size: " ,df.shape)
# print(" time:", time()-tos6)
#

# tos7 = time()
# print("7. keep only relevant columns...")
# df = s.leave_only_relevant_columns(f.after_text_preprocessing_fn)
# my.save_dataframe_to_file(df, f.short_df_fn)
# print(" done")
# print(" short dataframe size: ", df.shape)
# print(" time:", time()-tos7)


# tos8 = time()
# print("8. compile corpora and train w2v_model model... ")
# my_corpora = wm.gather_corpora_from_file(f.short_df_fn)
# wm.train_w2v_model(my_corpora)
# print(" done")
# print(" time:", time()-tos8)


tos9 = time()
print("10. START ADDING VECTORS")
w2v_model = Word2Vec.load("word2vec.model")

df_with_vectors = my.add_vectors_to_dataframe(f.short_df_fn, w2v_model)

print("adding vectors ... done")
print(" with vectors df size: ",  df_with_vectors.shape)

my.save_df_to_file(df_with_vectors, f.result_fn)
print(" dataset with vectors has been saved to file", f.result_fn)
print(" time:", time()-tos9)


# print("predict apgar using only numbers")
# p.predict_without_text(f.result_file_name)
# p.predict_with_text(f.result_file_name)

ttof = time()
print("TOTAL TIME ",  ttof - ttos)















