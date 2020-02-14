# 7 plot some statistic and correlation
# 8 leave only relevant column
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', None)

# read
file_name = "files/only_apgar.csv"
df = pd.read_csv(file_name)

df = df.rename(columns={'Возраст_мать': 'mother_age'})
df = df.rename(columns={'Антенатальная': 'antenal'})
df = df.rename(columns={'сзрп': 'szrp'})
df = df.rename(columns={'ОАА': 'OAA'})
df = df.rename(columns={'аборты': 'abortion'})
df = df.rename(columns={'кесарево': 'caesarean'})
df = df.rename(columns={'ГБ_насл': 'GB'})
df = df.rename(columns={'ИБС_насл': 'CHD'})
df = df.rename(columns={'Апгар1': 'target'})
df = df.fillna(0)



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
    ix = abs(correlated_df.corr()).sort_values('target', ascending=False).index
    correlated_df = correlated_df.loc[:, ix]
    cor = correlated_df[correlated_df.columns[0:]].corr()['target'][1:]
    cor = abs(cor)
    print(correlated_df.columns.values)
    cor.plot(kind='bar')
    plt.show()

    # print(correlated_df.info())
    # print(correlated_df.describe())



def plot_target_correlation_all():
    first_n_columns = 30
    correlated_df = df[df.columns.values]
    correlated_df = correlated_df.drop('Unnamed: 0', axis=1)
    correlated_df = correlated_df.drop('level_0', axis=1)
    correlated_df = correlated_df.drop('Unnamed: 0.1', axis=1)
    correlated_df = correlated_df.drop('index', axis=1)
    ix = abs(correlated_df.corr()).sort_values('target', ascending=False).index
    correlated_df = correlated_df.loc[:, ix]
    cor = correlated_df[correlated_df.columns[0:]].corr()['target'][1:first_n_columns]
    cor = abs(cor)
    cor.plot(kind='bar')
    print(correlated_df.iloc[:, 1:first_n_columns].columns.values)
    plt.show()
#


def get_short_df():
    return df[["target", "szrp", "OAA", "abortion", "caesarean", "GB", "CHD", "text_1", "text_2", "text_3", "text_4"]]


# plot_target_weight_bar()
# plot_weight_target_scatter()
# plot_height_target_scatter()
# plot_age_target_scatter()
plot_target_correlation_short()
plot_target_correlation_all()
# plot_full_correlation_matrix()

