import pandas as pd

full_dataset_file_name = "concatenated_results_no_duplicates.csv"
sheet_name = "concatenated_results_no_duplicates"
apgar1 = "Апгар1"
apgar2 = "Апгар2"


def save_to_file(dataframe):
    result_file_name = "apgar.csv"
    dataframe.to_csv(result_file_name)


def get_df_where_no_missin_values_in_column(dataset, column):
    df = dataset.dropna(subset=[column])
    df = df.reset_index()
    return df


def main():
    df = pd.read_csv(full_dataset_file_name)
    only_apgar_dataframe = get_df_where_no_missin_values_in_column(df, apgar1)
    save_to_file(only_apgar_dataframe)


main()
