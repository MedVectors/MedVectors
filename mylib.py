
import xlrd
import re
import numpy as np
from sklearn import metrics
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import preprocessing as pp

txt_file_name = "C:/Users/admin/Downloads/Telegram Desktop/anamnesis-fixed-perinatal.txt"
utf8 = "utf8"
xls_file_name = "C:/Users/admin/Downloads/Telegram Desktop/perinatal.xlsx"
sheet_name = "L1"
concatenated_dataframe_file_name = "files/result_no_duplicates.csv"
apgar_file_name = "files/only_apgar.csv"
relevant_columns_file_name = "files/short_dataset.csv"
cleaned_text_file_name = "files/cleaned_text.csv"
result_file_name = "files/final.csv"
cleaned2 = "files/cleaned2.csv"


def get_lines(filename):
    text = []
    with open(filename, "rb") as f:
        line = f.readline().decode('utf8')
        counter = 1
        while line:
            print(line)
            text.insert(counter, line.strip())
            line = f.readline().decode('utf8')# .decode(utf8)
            counter += 1
    return text


def print_lines(lines):
    for i in lines:
        print(i)


def split_lines(lines):
    splited_lines = []
    for string in lines:
        splited_lines.append(string.split())
    return splited_lines


def get_ids(list_for_ids):
    ids = []
    index = 0
    for i in list_for_ids:
        ids.insert(index, list_for_ids[index][0])
        index += 1
    return ids


def get_texts(list_for_texts):
    texts = []
    for i in list_for_texts:
        texts.append(re.sub("[^а-яА-Я]+", ' ', i))
    return texts


def combine_ids_and_texts(ids, texts):
    ids_and_texts = []
    index = 0
    for line in ids:
        ids_and_texts.insert(index, ("'" + ids[index].__str__() + "' , '" + texts[index].__str__() + "'"))
        index += 1
    return ids_and_texts


def get_list_of_ids_and_texts():
    list_for_texts = get_lines(txt_file_name).copy()
    list_for_ids = split_lines(list_for_texts.copy()).copy()
    ids_and_text = combine_ids_and_texts(get_ids(list_for_ids), get_texts(list_for_texts))
    return ids_and_text


def get_dataframe_from_txt():
    ids = get_ids(split_lines(get_lines(txt_file_name)))
    texts = get_texts(get_lines(txt_file_name))
    df = pd.DataFrame(list(zip(ids, texts)), columns=["id", "text"])
    for i in range(df.shape[0]):
        cur = df.loc[i]
        cur = pp.pre_processing(cur)
        print(i + 1, "out of ", df.shape[0], " ", cur[1])
        df.loc[i] = cur
    return df


def get_sheet_from_xls(file_name):
    wb = xlrd.open_workbook(file_name)
    sheet = wb.sheet_by_index(0)
    return sheet


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


# resulting method for reading xls file to dataframe
def get_dataframe_from_xls():
    return pd.read_excel(xls_file_name, sheet_name)


def drop_duplicate_line(df, dataset_size, new_col_name):
    index = 0
    while index < dataset_size:
        if df.loc[index, "id"] == df.loc[index + 1, "id"]:
            df.loc[index, new_col_name] = df.loc[index + 1, "text"]
            df = df.drop(index + 1)
            index += 1
        index += 1
    return df


def get_unduplicated_lines(df):
    print(" step 1")
    print("  rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.sort_values("id")
    df = drop_duplicate_line(df, df.shape[0] - 1, "t1")
    print("  duplicated: " + df["id"].duplicated().sum().__str__())

    print(" step 2")
    print("  rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.drop("level_0", 1)
    df = df.sort_values("id")
    df = drop_duplicate_line(df, df.shape[0] - 1, "t2")
    print("  duplicated: " + df["id"].duplicated().sum().__str__())

    print(" step 3")
    print("  rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.drop("level_0", 1)
    df = df.sort_values("id")
    df = drop_duplicate_line(df, df.shape[0] - 1, "t3")
    print("  duplicated: " + df["id"].duplicated().sum().__str__())

    print(" step 4")
    print("  rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.drop("level_0", 1)
    df = df.sort_values("id")
    df = drop_duplicate_line(df, df.shape[0] - 1, "t4")
    print("  duplicated: " + df["id"].duplicated().sum().__str__())

    print(" step 5")
    print("  rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.drop("level_0", 1)
    df = df.sort_values("id")
    df = drop_duplicate_line(df, df.shape[0] - 1, "t5")
    print("  duplicated: " + df["id"].duplicated().sum().__str__())

    print(" step 6")
    print("  rows: " + df.shape[0].__str__())
    df = df.reset_index()
    df = df.drop("level_0", 1)
    df = df.sort_values("id")
    df = drop_duplicate_line(df, df.shape[0] - 1, "t6")
    print("  duplicated: " + df["id"].duplicated().sum().__str__())

    return df


def save_dataframe_to_file(dataframe, file_name):
    dataframe.to_csv(file_name)


def concatenate_dataframes(df1, df2):
    result = pd.concat([df1, df2], axis=1, sort=True)
    return result


def get_specific_column_dataset(dataset_file_name, column):
    df = pd.read_csv(dataset_file_name)
    df = df.dropna(subset=[column])
    df = df.reset_index()
    return df


def leave_only_relevant_columns(file_name):
    df = pd.read_csv(file_name)

    df = df.rename(columns={'Возраст_мать': 'mother_age'})
    df = df.rename(columns={'Антенатальная': 'antenal'})
    df = df.rename(columns={'сзрп': 'szrp'})
    df = df.rename(columns={'ОАА': 'OAA'})
    df = df.rename(columns={'аборты': 'abortion'})
    df = df.rename(columns={'кесарево': 'caesarean'})
    df = df.rename(columns={'ГБ_насл': 'GB'})
    df = df.rename(columns={'ИБС_насл': 'CHD'})
    df = df.rename(columns={'Апгар1': 'apgar'})
    df = df.rename(columns={'text': 'text'})
    df = df.rename(columns={'t1': 'text_1'})
    df = df.rename(columns={'t2': 'text_2'})
    df = df.rename(columns={'t3': 'text_3'})
    df = df.rename(columns={'t4': 'text_4'})
    df = df.rename(columns={'t5': 'text_5'})
    df = df.rename(columns={'t6': 'text_6'})

    return df[["apgar", "szrp", "OAA", "abortion", "caesarean", "GB", "CHD", "text_1", "text_2", "text_3", "text_4"]] # ,  "text_5", "text_6"]]


def replace_nan_with_empty(df):
    for i in range(df.shape[0]):
        cur = df.loc[i, "text_1"]
        if cur == "nan nan nan nan":
            df.loc[i, "text_1"] = ""
    return df

def remove_single_letters(text):
    text = re.sub(r" а ", " ", text)
    text = re.sub(r" б ", " ", text)
    text = re.sub(r" в ", " ", text)
    text = re.sub(r" г ", " ", text)
    text = re.sub(r" д ", " ", text)
    text = re.sub(r" е ", " ", text)
    text = re.sub(r" ж ", " ", text)
    text = re.sub(r" э ", " ", text)
    text = re.sub(r" и ", " ", text)
    text = re.sub(r" к ", " ", text)
    text = re.sub(r" л ", " ", text)
    text = re.sub(r" м ", " ", text)
    text = re.sub(r" н ", " ", text)
    text = re.sub(r" о ", " ", text)
    text = re.sub(r" п ", " ", text)
    text = re.sub(r" р ", " ", text)
    text = re.sub(r" с ", " ", text)
    text = re.sub(r" т ", " ", text)
    text = re.sub(r" у ", " ", text)
    text = re.sub(r" ф ", " ", text)
    text = re.sub(r" х ", " ", text)
    text = re.sub(r" ц ", " ", text)
    text = re.sub(r" ч ", " ", text)
    text = re.sub(r" ш ", " ", text)
    text = re.sub(r" щ ", " ", text)
    text = re.sub(r" й ", " ", text)
    text = re.sub(r" э ", " ", text)
    text = re.sub(r" ю ", " ", text)
    text = re.sub(r" я ", " ", text)
    text = re.sub(r" ы ", " ", text)
    text = re.sub(r" ь ", " ", text)
    text = re.sub(r" ъ ", " ", text)
    return text

def remove_spaces(df):
    for i in range(df.shape[0]):
        text = df.loc[i, "text_1"]
        text = "  " + text
        text = re.sub(r"nan", "", text)
        text = text.lower()
        text = remove_single_letters(text)
        text = remove_single_letters(text)
        text = text.strip()
        text = re.sub(r"  ", "", text)
        df.loc[i, "text_1"] = text
        return df


def put_text_in_one_colunm(file_name):
    df = pd.read_csv(file_name)
    df = df.drop("Unnamed: 0", axis=1)
    df = df.rename(columns={'target': 'apgar'})

    df['target'] = df['apgar'].apply(lambda x: 1 if x > 7 else 0)
    df = df.drop("apgar", axis=1)
    # print(df[['target']].sum())

    df_text = df.copy()
    df_text["text_1"] = df_text["text_1"].astype(str)
    df_text["text_2"] = df_text["text_2"].astype(str)
    df_text["text_3"] = df_text["text_3"].astype(str)
    df_text["text_4"] = df_text["text_4"].astype(str)
    df_text["text_1"] = df_text["text_1"] + " " + df_text["text_2"]
    df_text["text_1"] = df_text["text_1"] + " " + df_text["text_3"]
    df_text["text_1"] = df_text["text_1"] + " " + df_text["text_4"]

    df_text = replace_nan_with_empty(df_text)
    df_text = remove_spaces(df_text)
    df_text = df_text.rename(columns={'text_1': 'text'})
    df_text = df_text.drop("text_2", axis=1)
    df_text = df_text.drop("text_3", axis=1)
    df_text = df_text.drop("text_4", axis=1)

    df_text = df_text.dropna(how='any', subset=['text'])

    print(df_text)

    return df_text


def print_all_not_empty_text(text):
    for i in range(text.shape[0]):
        cur = text.loc[i, "text_1"]
        if cur != "":
            print(str(i) + ":  " + str(cur))


def get_text_df(file_name):
    dataframe = pd.read_csv(file_name)
    dataframe = dataframe.drop("Unnamed: 0", axis=1)
    dataframe = dataframe.dropna(how='any', subset=['text'])
    dataframe = dataframe.reset_index()
    return dataframe

def gather_corpora_from_file(file_name):
    # dataframe = get_text_df(file_name)
    dataframe = pd.read_csv(file_name)
    print("dataframe ", dataframe)
    corpora = []
    for i in range(dataframe.shape[0]):
        cur = dataframe.loc[i, "text"]
        cur = cur.split()
        corpora.insert(i, cur)
        # print(corpora)
    return corpora

def get_word2vec_model(corpora):
    path = get_tmpfile("word2vec.model")
    model = Word2Vec(corpora, size=100, window=3, min_count=1, workers=4)
    model.train(corpora, total_examples=model.corpus_count, epochs=model.corpus_count)
    model.save("word2vec.model")
    return model

def add_vectors_to_dataframe(file_name, w2v_model):
    dataframe = pd.read_csv(file_name)
    dataframe = dataframe.drop("Unnamed: 0", axis=1)
    dataframe = dataframe.dropna(how='any', subset=['text'])
    dataframe = dataframe.reset_index()

    print(dataframe.shape[0])

    print("======start adding vectors to dataset========")
    for i in range(dataframe.shape[0]):
        cur = dataframe.loc[i, "text"]
        cur = cur.split()
        print("  element " + str(i) + " of " + str(dataframe.shape[0]))
        leng = 0
        if len(cur) > 100:
            leng = 100
        else:
            leng = len(cur)
        for j in range(leng):
            for v in range(100):
                dataframe.loc[i, j * 100 + v + 8] = w2v_model.wv[str(cur[j])][v]
        print("len = ", leng)
        # else:
            # print(str(i) + " not included--")
    return dataframe

def print_scores(clf, y_train, y_test, x_train, x_test):

    predicted_train = clf.predict(x_train)
    predicted_test = clf.predict(x_test)

    accuracy_train = accuracy_score(predicted_train, y_train)
    accuracy_test = accuracy_score(predicted_test, y_test)

    print("ACC TEST: " + str(accuracy_test))
    print("ACC TRAIN: " + str(accuracy_train))

    fpr, tpr, _ = metrics.roc_curve(np.array(y_train), clf.predict_proba(x_train)[:, 1])
    auc_train = metrics.auc(fpr, tpr)

    fpr, tpr, _ = metrics.roc_curve(np.array(y_test), clf.predict_proba(x_test)[:, 1])
    auc_test = metrics.auc(fpr, tpr)

    print("AUC TEST: " + str(auc_test))
    print("AUC TRAIN: " + str(auc_train))

    auc_roc_test = metrics.roc_auc_score(y_test, predicted_test)
    auc_roc_train = metrics.roc_auc_score(y_train, predicted_train)

    print("ACC TEST: " + str(auc_roc_test))
    print("ACC TRAIN: " + str(auc_roc_train))

    average_precision_test = metrics.average_precision_score(y_test, predicted_test)
    average_precision_train = metrics.average_precision_score(y_train, predicted_train)

    print("average_precision TEST: " + str(average_precision_test))
    print("average_precision TRAIN: " + str(average_precision_train))



def predict_without_text(file_name):
    print("==============================================================")
    print("prediction (no text)...")

    df = pd.read_csv(file_name)

    # TODO
    df = df.fillna(0)

    # split
    y = df["target"]
    X = df.iloc[:, 3:9]  # without target and without texts
    X = X.fillna(0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    predicted_train = clf.predict(X_train)
    predicted_test = clf.predict(X_test)

    target_names = ['class 0', 'class 1']
    print(classification_report(y_test, predicted_test, target_names=target_names))

def predict_with_text(file_name):
    df = pd.read_csv(file_name)
    print("==============================================================")
    print("prediction with text")

    # split
    y = df["target"]
    x = df.copy()
    x = x.iloc[:, 3:]
    x = x.drop("target", axis=1)
    x = x.drop("text", axis=1)
    x = x.fillna(0)

    x = x.iloc[:,:4000]

    # print(x)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=7)

    clf = RandomForestClassifier()
    clf.fit(x_train, y_train)

    predicted_train = clf.predict(x_train)
    predicted_test = clf.predict(x_test)

    target_names = ['class 0', 'class 1']
    print(classification_report(y_test, predicted_test, target_names=target_names))


def predict_by_nn(file_name):
    df = pd.read_csv(file_name)

    # split
    y = df["target"]
    x = df.copy()
    x = x.iloc[:, 3:]
    x = x.drop("target", axis=1)
    x = x.drop("text", axis=1)
    x = x.fillna(0)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=257)

    # define the keras model
    model = Sequential()
    model.add(Dense((x_train.shape[1] // 2), input_dim=x_train.shape[1], activation='relu'))
    model.add(Dense(10, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    history =  model.fit(x_train, y_train, validation_split=0.33, epochs=15, batch_size=200, verbose=1)

    predicted_train = model.predict(x_train)
    predicted_test = model.predict(x_test)

    target_names = ['class 0', 'class 1']
    # print(classification_report(y_test, predicted_test, target_names=target_names))

    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()
