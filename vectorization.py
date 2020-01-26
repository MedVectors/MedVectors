# 11.
import pandas as pd
from gensim.test.utils import get_tmpfile
from gensim.models import Word2Vec


# pd.set_option('display.max_columns', None)

def read_file():
    file_name = "cleaned_text.csv"
    dataframe = pd.read_csv(file_name)
    dataframe = dataframe.drop("Unnamed: 0", axis=1)
    # Drop rows with any NaN in column text
    dataframe = dataframe.dropna(how='any', subset=['text'])
    dataframe = dataframe.reset_index()
    dataframe = dataframe.drop(dataframe.index[1])
    dataframe = dataframe.drop(dataframe.index[12])
    dataframe = dataframe.drop(dataframe.index[34])
    dataframe = dataframe.drop(dataframe.index[154])
    dataframe = dataframe.drop(dataframe.index[953])  # incredibly slow
    dataframe = dataframe.reset_index()
    return dataframe


def gather_corpora():
    corpora = []
    for i in range(df.shape[0]):
        cur = df.loc[i, "text"]
        cur = cur.split()
        corpora.insert(i, cur)
        return corpora


def get_vword2vec_model():
    path = get_tmpfile("word2vec.model")
    model = Word2Vec(my_text, size=100, window=5, min_count=1, workers=4)
    model.train(my_text, total_examples=model.corpus_count, epochs=model.corpus_count)
    model.save("word2vec.model")
    return model


def add_vectors_to_dataframe():
    print("======start adding vectors to dataset========")
    for i in range(df.shape[0]):
        cur = df.loc[i, "text"]
        cur = cur.split()
        print("element " + str(i) + " of " + str(df.shape[0]))
        if len(cur) < 30:
            for j in range(len(cur)):
                for v in range(100):
                    df.loc[i, j * 100 + v + 8] = w2v_model.wv[str(cur[j])][v]
        else:
            print("not included -----------------------------------------------------------" + str(i))


df = read_file()
print("read file... done")
my_text = gather_corpora()
print("compile corpora... done")
w2v_model = get_vword2vec_model()
print("train model... done")
add_vectors_to_dataframe()
print("adding vectors ... done")

result_file_name = "final.csv"
df.to_csv(result_file_name)
print("dataset has been saved to file")
