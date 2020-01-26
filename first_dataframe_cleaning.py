# 6. remove lines where APGAR in not presented
import pandas as pd

dataset_file_name = "concatenated_results_no_duplicates.csv"


def save_to_file(dataframe, file_name):
    result_file_name = file_name
    dataframe.to_csv(result_file_name)


def get_df_where_no_missing_values_in_column(dataset, column):
    df = dataset.dropna(subset=[column])
    df = df.reset_index()
    return df


def main():
    df = pd.read_csv(dataset_file_name)
    only_apgar_dа = get_df_where_no_missing_values_in_column(df, "Апгар1")
    save_to_file(dataframe=only_apgar_dа, file_name="apgar.csv")


main()
