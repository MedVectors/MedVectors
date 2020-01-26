import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)

# read
file_name = "apgar3.csv"
df = pd.read_csv(file_name)

df = df.rename(columns={'Возраст_мать': 'mother_age'})
df = df.rename(columns={'Антенатальная': 'antenal'})
df = df.rename(columns={'сзрп': 'szrp'})
df = df.rename(columns={'ОАА': 'OAA'})
df = df.rename(columns={'аборты': 'abortion'})
df = df.rename(columns={'кесарево': 'caesarean'})
df = df.rename(columns={'ГБ_насл': 'GB'})
df = df.rename(columns={'ИБС_насл': 'CHD'})

print(df.columns)


def plot_full_correlation_matrix():
    correlation = df.corr()
    plt.matshow(correlation)
    cb = plt.colorbar()
    plt.show()


def plot_weight_target_scatter():
    df.plot(kind='scatter', x="вес", y="target")
    plt.show()


def plot_target_weight_bar():
    df.plot(kind='bar', x="target", y="вес")
    plt.show()


def plot_height_target_scatter():
    df.plot(kind='scatter', x="рост", y="target")
    plt.show()


def plot_age_target_scatter():
    df.plot(kind='scatter', x="mother_age", y="target")
    plt.show()


def plot_grouped_mother_age():
    df[['mother_age']].plot(kind='hist', bins=[15, 20, 25, 30, 35, 40, 45, 50, 55], rwidth=0.8)
    plt.show()


def plot_grouped_target():
    df[['target']].plot(kind='hist', rwidth=0.8)
    plt.show()


def plot_target_correlations():
    cor_df = df.iloc[:, :60]
    cor = cor_df[cor_df.columns[1:]].corr()['target'][1:]
    cor = abs(cor)
    cor.plot(kind='bar')
    plt.show()


def plot_target_correlation_short():
    correlated_df = df[["target", "szrp", "OAA", "abortion", "caesarean", "GB", "CHD"]]
    cor = correlated_df[correlated_df.columns[0:]].corr()['target'][1:]
    cor = abs(cor)
    cor.plot(kind='bar')
    plt.show()


def get_short_df():
    return df[["target", "szrp", "OAA", "abortion", "caesarean", "GB", "CHD", "text_1", "text_2", "text_3", "text_4"]]


# plot_target_weight_bar()
# plot_weight_target_scatter()
# plot_height_target_scatter()
# plot_age_target_scatter()
# plot_target_correlations()

result_file_name = "short_dataset.csv"
get_short_df().to_csv(result_file_name)
