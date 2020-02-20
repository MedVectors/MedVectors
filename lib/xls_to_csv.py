import pandas as pd
from files import file_names as f
import lib.mylib as my


def read_xls():
    df_xls = pd.read_excel(f.xls_file_name, f.sheet_name)
    df_xls = df_xls.set_index(df_xls.loc[:, "m_id"].values)
    df_xls.drop("неделя", axis=1, inplace=True)
    df_xls["Беременность номер"].fillna(1, inplace=True)
    df_xls.fillna(0, inplace=True)
    df_xls['Резус_ребенок'] = df_xls['Резус_ребенок'].map({'RhPlus': 1, 'RhMin': 2})
    df_xls['Резус_ребенок'].fillna(0, inplace=True)
    df_xls["rezus_child_known"] = df_xls['Резус_ребенок'].map({0:0, 1:1, 2:1})
    df_xls['Резус_мать'] = df_xls['Резус_мать'].map({'RhPlus': 1, 'RhMin': 2})
    df_xls['Резус_мать'].fillna(0, inplace=True)
    df_xls["rezus_mather_known"] = df_xls['Резус_мать'].map({0:0, 1:1, 2:1})
    df_xls['Кто_принял_роды'].fillna(0, inplace=True)
    df_xls["Кто_принял_роды"] = df_xls['Кто_принял_роды'].map({"акушерка":1, "врач":2, "другое_лицо":0, "фельдшер":0})
    df_xls.drop("Дата смерти", axis=1, inplace=True)
    df_xls.drop("Время смерти", axis=1, inplace=True)
    df_xls.drop("дата", axis=1, inplace=True)
    df_xls.drop("состояние_ребенок_мертв", axis=1, inplace=True)
    df_xls.drop("диагноз_ребенок", axis=1, inplace=True)
    df_xls.drop("расшифровка_диагноза_ребенок", axis=1, inplace=True)
    df_xls.drop("Результат лечения", axis=1, inplace=True)
    df_xls.drop("причина", axis=1, inplace=True)
    df_xls.drop("Для_флага_выбора_одноплодных_родов", axis=1, inplace=True)
    df_xls.drop("Дата время рождения", axis=1, inplace=True)
    df_xls.drop("дата рождения мамы", axis=1, inplace=True)
    df_xls.drop("срок", axis=1, inplace=True)
    my.save_dataframe_to_file(df_xls, f.xls_to_csv_fn)
