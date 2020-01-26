import re

import pandas as pd
import numpy as np
import matplotlib.pyplot
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import metrics

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)

file_name = "short_dataset.csv"


def read_data():
    df = pd.read_csv(file_name)
    df = df.drop("Unnamed: 0", axis=1)
    df = df.rename(columns={'target': 'apgar'})

    # target binarization
    df['target'] = df['apgar'].apply(lambda x: 1 if x > 7 else 0)
    df = df.drop("apgar", axis=1)
    return df


def put_text_in_one_colunm():
    df_text = df.copy()

    df_text["text_1"] = df_text["text_1"].astype(str)
    df_text["text_2"] = df_text["text_2"].astype(str)
    df_text["text_3"] = df_text["text_3"].astype(str)
    df_text["text_4"] = df_text["text_4"].astype(str)

    df_text["text_1"] = df_text["text_1"] + " " + df_text["text_2"]
    df_text["text_1"] = df_text["text_1"] + " " + df_text["text_3"]
    df_text["text_1"] = df_text["text_1"] + " " + df_text["text_4"]
    # print(df_text.loc[:, "text_1"])
    return df_text


def print_all_not_empty_text(text):
    for i in range(text.shape[0]):
        cur = text.loc[i, "text_1"]
        if cur != "":
            print(str(i) + ":  " + str(cur))


def predict_without_text():
    print("==============================================================")
    print("start prediction part...")

    # split
    y = df["target"]
    X = df.iloc[:, :-5]  # without target and without texts
    X = X.fillna(0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    predicted_train = clf.predict(X_train)
    predicted_test = clf.predict(X_test)

    accuracy_train = accuracy_score(predicted_train, y_train)
    accuracy_test = accuracy_score(predicted_test, y_test)

    print("ACC TEST: " + str(accuracy_test))
    print("ACC TRAIN: " + str(accuracy_train))

    fpr, tpr, _ = metrics.roc_curve(np.array(y_train), clf.predict_proba(X_train)[:, 1])
    auc_train = metrics.auc(fpr, tpr)

    fpr, tpr, _ = metrics.roc_curve(np.array(y_test), clf.predict_proba(X_test)[:, 1])
    auc_test = metrics.auc(fpr, tpr)

    print("AUC TEST: " + str(auc_test))
    print("AUC TRAIN: " + str(auc_train))


# replace nan with empty
def replace_nan_with_empty():
    for i in range(df_text.shape[0]):
        cur = df_text.loc[i, "text_1"]
        if cur == "nan nan nan nan":
            df_text.loc[i, "text_1"] = ""


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


def remove_spaces():
    for i in range(df_text.shape[0]):
        text = df_text.loc[i, "text_1"]
        text = "  " + text
        text = re.sub(r"nan", "", text)
        text = text.lower()
        text = remove_single_letters(text)
        text = remove_single_letters(text)
        text = text.strip()
        text = re.sub(r"  ", "", text)
        df_text.loc[i, "text_1"] = text


def rename_column(df_text):
    df_text = df_text.drop("text_2", axis=1)
    df_text = df_text.drop("text_3", axis=1)
    df_text = df_text.drop("text_4", axis=1)
    return df_text


def delete_columns(df_text):
    df_text = df_text.rename(columns={'text_1': 'text'})
    return df_text


df = read_data()
df_text = put_text_in_one_colunm()
replace_nan_with_empty()
remove_spaces()
print_all_not_empty_text(df_text)
df_text = rename_column(df_text)
df_text = delete_columns(df_text)

predict_without_text()

# print(df_text)
#
# result_file_name = "cleaned_text.csv"
# df_text.to_csv(result_file_name)
