from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec
import pandas as pd
from lib import preprocessing as pp


def save_df_to_file(dataframe, file_name):
    dataframe.to_csv(file_name)


def preprocess(fn):
    df = pd.read_csv(fn, index_col=0)
    df = pp.pre_processing(df[["text", "t1","t2","t3","t4","t5","t6","t7","t8","t9","t10","t11","t12","t13","t14","t15","t16","t17","t18","t19"]])
    return df


def leav_only_overlap_rows(dataset_file_name):
    df = pd.read_csv(dataset_file_name, index_col=0)
    df = df.dropna(subset=["Апгар1"])
    df = df.dropna(subset=["id"])
    return df


def print_lines(lines):
    for i in lines:
        print(i)

def get_dead_indexes(sheet):
    dead = []
    for i in range(sheet.nrows):
        if sheet.cell_value(i, 23) != "":
            print(i, sheet.cell_value(i, 23))
            dead.append(i)
    return dead


def print_sheet_information(sheet):
    print("Строк всего " + sheet.nrows.__str__())
    print("Столбцов всего " + sheet.ncols.__str__())

    print("НАЗВАНИЯ СТОЛБЦОВ")
    for i in range(sheet.ncols):
        print(i, sheet.cell_value(0, i))

    print("Содержимое строки 1")
    print(sheet.row_values(0))

    print("строки где смерть")
    for i in get_dead_indexes(sheet):
        print(sheet.row_values(i))





# def concatenate_dataframes(df1, df2):
#     result = pd.concat([df1, df2], axis=1, sort=True)
#     return result


# def get_lines(filename):
#     text = []
#     with open(filename, "rb") as f:
#         line = f.readline().decode('utf8')
#         counter = 1
#         while line:
#             # print(line)
#             text.insert(counter, line.strip())
#             line = f.readline().decode('utf8')# .decode(utf8)
#             counter += 1
#     return text

# def split_lines(lines):
#     splited_lines = []
#     for string in lines:
#         splited_lines.append(string.split())
#     return splited_lines


# def get_ids(list_for_ids):
#     ids = []
#     index = 0
#     for i in list_for_ids:
#         ids.insert(index, list_for_ids[index][0])
#         index += 1
#     return ids


# def get_texts(list_for_texts):
#     texts = []
#     for i in list_for_texts:
#         texts.append(re.sub("[^а-яА-Я]+", ' ', i))
#     return texts

#
# def combine_ids_and_texts(ids, texts):
#     ids_and_texts = []
#     index = 0
#     for line in ids:
#         ids_and_texts.insert(index, ("'" + ids[index].__str__() + "' , '" + texts[index].__str__() + "'"))
#         index += 1
#     return ids_and_texts

#
# def get_list_of_ids_and_texts():
#     list_for_texts = get_lines(f.txt_file_name).copy()
#     list_for_ids = split_lines(list_for_texts.copy()).copy()
#     ids_and_text = combine_ids_and_texts(get_ids(list_for_ids), get_texts(list_for_texts))
#     return ids_and_text



# def get_dataframe_from_txt():
#     ids = get_ids(split_lines(get_lines(f.txt_file_name)))
#     texts = get_texts(get_lines(f.txt_file_name))
#     df = pd.DataFrame(list(zip(ids, texts)), columns=["id", "text"])
#     return df


# def get_sheet_from_xls(file_name):
#     wb = xlrd.open_workbook(file_name)
#     sheet = wb.sheet_by_index(0)
#     return sheet




# resulting method for reading xls file to dataframe
# def get_dataframe_from_xls():
#     return pd.read_excel(f.xls_file_name, f.sheet_name)
#

# def drop_duplicate_line(df, new_col_name):
#     index = 0
#     while index < df.shape[0]-1:
#         if df.loc[index, "id"] == df.loc[index + 1, "id"]:
#             df.loc[index, new_col_name] = df.loc[index + 1, "text"]
#             df = df.drop(index + 1)
#             index += 1
#         index += 1
#     return df

#
# def get_unduplicated_lines():
#     df = pd.read_csv( f.id_and_text_fn)
#     tos = time()
#     print(" step 1")
#     print("  rows: " + df.shape[0].__str__())
#     df = df.reset_index()
#     df = df.sort_values("id")
#     df = drop_duplicate_line(df, df.shape[0] - 1, "t1")
#     print("  duplicated: " + df["id"].duplicated().sum().__str__())
#     print("time for step 1 ", time()-tos)
#
#     tos = time()
#     print(" step 2")
#     print("  rows: " + df.shape[0].__str__())
#     df = df.reset_index()
#     df = df.drop("level_0", 1)
#     df = df.sort_values("id")
#     df = drop_duplicate_line(df, df.shape[0] - 1, "t2")
#     print("  duplicated: " + df["id"].duplicated().sum().__str__())
#     print("time for step 2 ", time()-tos)
#
#     tos = time()
#     print(" step 3")
#     print("  rows: " + df.shape[0].__str__())
#     df = df.reset_index()
#     df = df.drop("level_0", 1)
#     df = df.sort_values("id")
#     df = drop_duplicate_line(df, df.shape[0] - 1, "t3")
#     print("  duplicated: " + df["id"].duplicated().sum().__str__())
#     print("time for step 3 ", time()-tos)
#
#     tos = time()
#     print(" step 4")
#     print("  rows: " + df.shape[0].__str__())
#     df = df.reset_index()
#     df = df.drop("level_0", 1)
#     df = df.sort_values("id")
#     df = drop_duplicate_line(df, df.shape[0] - 1, "t4")
#     print("  duplicated: " + df["id"].duplicated().sum().__str__())
#     print("time for step 4 ", time()-tos)
#
#     tos = time()
#     print(" step 5")
#     print("  rows: " + df.shape[0].__str__())
#     df = df.reset_index()
#     df = df.drop("level_0", 1)
#     df = df.sort_values("id")
#     df = drop_duplicate_line(df, df.shape[0] - 1, "t5")
#     print("  duplicated: " + df["id"].duplicated().sum().__str__())
#     print("time for step 5 ", time()-tos)
#
#     tos = time()
#     print(" step 6")
#     print("  rows: " + df.shape[0].__str__())
#     df = df.reset_index()
#     df = df.drop("level_0", 1)
#     df = df.sort_values("id")
#     df = drop_duplicate_line(df, df.shape[0] - 1, "t6")
#     print("  duplicated: " + df["id"].duplicated().sum().__str__())
#     print("time for step 6 ", time()-tos)
#
#     return df




# def leave_only_relevant_columns(file_name):
#     df = pd.read_csv(file_name, index_col=0)
#     df = df.rename(columns={'Возраст_мать': 'mother_age'})
#     df = df.rename(columns={'Антенатальная': 'antenal'})
#     df = df.rename(columns={'сзрп': 'szrp'})
#     df = df.rename(columns={'ОАА': 'OAA'})
#     df = df.rename(columns={'аборты': 'abortion'})
#     df = df.rename(columns={'кесарево': 'caesarean'})
#     df = df.rename(columns={'ГБ_насл': 'GB'})
#     df = df.rename(columns={'ИБС_насл': 'CHD'})
#     df = df.rename(columns={'Апгар1': 'apgar'})
#     df['target'] = df['apgar'].apply(lambda x: 1 if x > 7 else 0)
#     df = df[["target", "szrp", "OAA", "abortion", "caesarean", "GB", "CHD", "text"]]
#     print(df)
#     return df


# def replace_nan_with_empty(df):
#     for i in range(df.shape[0]):
#         cur = df.loc[i, "text"]
#         if cur == "nan nan nan nan":
#             df.loc[i, "text_1"] = ""
#     return df

# def remove_single_letters(text):
#     text = re.sub(r" а ", " ", text)
#     text = re.sub(r" б ", " ", text)
#     text = re.sub(r" в ", " ", text)
#     text = re.sub(r" г ", " ", text)
#     text = re.sub(r" д ", " ", text)
#     text = re.sub(r" е ", " ", text)
#     text = re.sub(r" ж ", " ", text)
#     text = re.sub(r" э ", " ", text)
#     text = re.sub(r" и ", " ", text)
#     text = re.sub(r" к ", " ", text)
#     text = re.sub(r" л ", " ", text)
#     text = re.sub(r" м ", " ", text)
#     text = re.sub(r" н ", " ", text)
#     text = re.sub(r" о ", " ", text)
#     text = re.sub(r" п ", " ", text)
#     text = re.sub(r" р ", " ", text)
#     text = re.sub(r" с ", " ", text)
#     text = re.sub(r" т ", " ", text)
#     text = re.sub(r" у ", " ", text)
#     text = re.sub(r" ф ", " ", text)
#     text = re.sub(r" х ", " ", text)
#     text = re.sub(r" ц ", " ", text)
#     text = re.sub(r" ч ", " ", text)
#     text = re.sub(r" ш ", " ", text)
#     text = re.sub(r" щ ", " ", text)
#     text = re.sub(r" й ", " ", text)
#     text = re.sub(r" э ", " ", text)
#     text = re.sub(r" ю ", " ", text)
#     text = re.sub(r" я ", " ", text)
#     text = re.sub(r" ы ", " ", text)
#     text = re.sub(r" ь ", " ", text)
#     text = re.sub(r" ъ ", " ", text)
#     return text

# def remove_spaces(df):
#     for i in range(df.shape[0]):
#         text = df.loc[i, "text_1"]
#         text = "  " + text
#         text = re.sub(r"nan", "", text)
#         text = text.lower()
#         text = remove_single_letters(text)
#         text = remove_single_letters(text)
#         text = text.strip()
#         text = re.sub(r"  ", "", text)
#         df.loc[i, "text_1"] = text
#         return df


# def put_text_in_one_colunm(file_name):
#     df = pd.read_csv(file_name)
#     df = df.drop("Unnamed: 0", axis=1)
#     df = df.rename(columns={'target': 'apgar'})
#
#     df['target'] = df['apgar'].apply(lambda x: 1 if x > 7 else 0)
#     df = df.drop("apgar", axis=1)
#     # print(df[['target']].sum())
#
#     df_text = df.copy()
#     df_text["text_1"] = df_text["text_1"].astype(str)
#     df_text["text_2"] = df_text["text_2"].astype(str)
#     df_text["text_3"] = df_text["text_3"].astype(str)
#     df_text["text_4"] = df_text["text_4"].astype(str)
#     df_text["text_1"] = df_text["text_1"] + " " + df_text["text_2"]
#     df_text["text_1"] = df_text["text_1"] + " " + df_text["text_3"]
#     df_text["text_1"] = df_text["text_1"] + " " + df_text["text_4"]
#
#     df_text = replace_nan_with_empty(df_text)
#     df_text = remove_spaces(df_text)
#     df_text = df_text.rename(columns={'text_1': 'text'})
#     df_text = df_text.drop("text_2", axis=1)
#     df_text = df_text.drop("text_3", axis=1)
#     df_text = df_text.drop("text_4", axis=1)
#
#     df_text = df_text.dropna(how='any', subset=['text'])
#     df_text = df_text.reset_index()
#
#     # print(df_text)
#
#     return df_text


# def print_all_not_empty_text(text):
#     for i in range(text.shape[0]):
#         cur = text.loc[i, "text_1"]
#         if cur != "":
#             print(str(i) + ":  " + str(cur))


# def gather_corpora_from_file(file_name):
#     df = pd.read_csv(file_name, index_col=0)
#     corpora = []
#     df = df.reset_index()
#     for i in range(df.shape[0]):
#         cur = df.loc[i, "text"]
#         cur = cur.split()
#         corpora.insert(i, cur)
#     return corpora

# def get_word2vec_model(corpora):
#     path = get_tmpfile("word2vec.model")
#     model = Word2Vec(corpora, size=100, window=3, min_count=3, workers=4)
#
#     print("model: ")
#     print(model)
#     print("model corpus_count " , model.corpus_count)
#
#     model.train(corpora, total_examples=model.corpus_count, epochs=model.corpus_count)
#     model.save("word2vec.model")
#     return model

def add_vectors_to_dataframe(file_name, w2v_model):
    df = pd.read_csv(file_name, index_col=0)
    df = df.reset_index()
    number_of_rows = df.shape[0]
    number_of_columns = df.shape[1]
    word_vectors = w2v_model.wv

    print("======start adding vectors to dataset========")
    for current_row in range(number_of_rows):
        current_str = str(df.loc[current_row, "text"])
        current_str = current_str.split()
        print("  element ", current_row, " of ", number_of_rows)
        if len(current_str) > 100:
            leng_of_str = 100
        else:
            leng_of_str = len(current_str)

        for word_number in range(leng_of_str):
            if str(current_str[word_number]) in word_vectors.vocab:
                for element_of_vector in range(w2v_model.vector_size):
                    df.loc[current_row, word_number * w2v_model.vector_size + element_of_vector + number_of_columns] \
                            = w2v_model.wv[str(current_str[word_number])][element_of_vector]
            else:
                print("not in vocab ", str(current_str[word_number]))
        print("len = ", leng_of_str)
    return df




