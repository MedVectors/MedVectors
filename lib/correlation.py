import pandas as pd


def leave_only_relevant_columns(file_name):
    df = pd.read_csv(file_name, index_col=0)
    df = df.rename(columns={'Возраст_мать': 'mother_age'})
    df = df.rename(columns={'Антенатальная': 'antenal'})
    df = df.rename(columns={'сзрп': 'szrp'})
    df = df.rename(columns={'ОАА': 'OAA'})
    df = df.rename(columns={'аборты': 'abortion'})
    df = df.rename(columns={'кесарево': 'caesarean'})
    df = df.rename(columns={'ГБ_насл': 'GB'})
    df = df.rename(columns={'ИБС_насл': 'CHD'})
    df = df.rename(columns={'Апгар1': 'apgar'})
    df['target'] = df['apgar'].apply(lambda x: 1 if x > 7 else 0)
    df = df[["target", "szrp", "OAA", "abortion", "caesarean", "GB", "CHD", "text"]]
    return df