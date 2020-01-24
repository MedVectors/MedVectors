import pandas as pd
import numpy as np
import matplotlib.pyplot
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import metrics

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)

# read dataset
file_name = "short_dataset.csv"
df = pd.read_csv(file_name)
df = df.drop("Unnamed: 0", axis=1)
df = df.rename(columns={'target' : 'apgar'})

# predict without text
# target binarization
df['target'] = df['apgar'].apply(lambda x: 1 if x > 7 else 0)
# print(df[["target2","target"]])
df = df.drop("apgar", axis=1)

print("==============================================================")
print("start prediction part...")

# split
y = df["target"]
X = df.iloc[:,:-5]
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

fpr, tpr, _ = metrics.roc_curve(np.array(y_train), clf.predict_proba(X_train)[:,1])
auc_train = metrics.auc(fpr,tpr)

fpr, tpr, _ = metrics.roc_curve(np.array(y_test), clf.predict_proba(X_test)[:,1])
auc_test = metrics.auc(fpr,tpr)

print("AUC TEST: " + str(auc_test))
print("AUC TRAIN: " + str(auc_train))

# train model
# get score


# predict with text
# train with text
# get score




# plot two scores in one plot