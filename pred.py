from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
import mylib as my
import pandas as pd

pd.set_option('display.max_columns', 10000)

# my.predict_without_text(my.result_file_name)
# my.predict_with_text(my.result_file_name)
my.predict_by_nn(my.result_file_name)

