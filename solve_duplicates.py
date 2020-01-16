from numba import jit, cuda
import numba  # We added these two lines for a 500x speedup

    # We added these two lines for a 500x speedup
import read_txt as txt
import pandas as pd
pd.set_option('display.max_columns', 30)

test_df = txt.get_dataframe_from_txt()

print("rows: " + test_df.shape[0].__str__())

@numba.jit
def run(df, number_of_iterations, col_name):
    index = 0
    while index < number_of_iterations:
        if df.loc[index, "id"] == df.loc[index + 1, "id"]:
            df.loc[index, col_name] = df.loc[index + 1, "text"]
            df = df.drop(index + 1)
            index += 1
        index += 1
    return df

print("rows: " + test_df.shape[0].__str__())
test_df = test_df.reset_index()
test_df = test_df.sort_values("id")
test_df = run(test_df, test_df.shape[0]-1, "t1")
print("duplicated: " + test_df["id"].duplicated().sum().__str__())


print("rows: " + test_df.shape[0].__str__())
test_df = test_df.reset_index()
test_df = test_df.drop("level_0", 1)
test_df = test_df.sort_values("id")
test_df = run(test_df, test_df.shape[0]-1, "t2")
# print(test_df.head(15))
# print(test_df["id"].duplicated())
print("duplicated: " + test_df["id"].duplicated().sum().__str__())

print("rows: " + test_df.shape[0].__str__())
test_df = test_df.reset_index()
test_df = test_df.drop("level_0", 1)
test_df = test_df.sort_values("id")
test_df = run(test_df, test_df.shape[0]-1, "t3")
# print(test_df.head(15))
# print(test_df["id"].duplicated())
print("duplicated: " + test_df["id"].duplicated().sum().__str__())

print("rows: " + test_df.shape[0].__str__())
test_df = test_df.reset_index()
test_df = test_df.drop("level_0", 1)
test_df = test_df.sort_values("id")
test_df = run(test_df, test_df.shape[0]-1, "t4")
# print(test_df.head(15))
# print(test_df["id"].duplicated())
print("duplicated: " + test_df["id"].duplicated().sum().__str__())


print("rows: " + test_df.shape[0].__str__())
test_df = test_df.reset_index()
test_df = test_df.drop("level_0", 1)
test_df = test_df.sort_values("id")
test_df = run(test_df, test_df.shape[0]-1, "t5")
# print(test_df.head(15))
# print(test_df["id"].duplicated())
print("duplicated: " + test_df["id"].duplicated().sum().__str__())


print("rows: " + test_df.shape[0].__str__())
test_df = test_df.reset_index()
test_df = test_df.drop("level_0", 1)
test_df = test_df.sort_values("id")
test_df = run(test_df, test_df.shape[0]-1, "t6")
# print(test_df.head(15))
# print(test_df["id"].duplicated())
print("duplicated: " + test_df["id"].duplicated().sum().__str__())



print(test_df)