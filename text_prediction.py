from docutils.nodes import Sequential
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df = pd.read_csv("final.csv")
df = df.drop("Unnamed: 0", axis=1)
df = df.drop("level_0", axis=1)
df = df.dropna(how='any', subset=['200'])
df = df.reset_index()
print(df)


def predict_random_forest():
    print("==============================================================")
    print("start prediction part...")

    # split
    y = df["target"]
    X = df.copy()
    X = df.drop("target", axis=1)
    X = df.drop("text", axis=1)
    X = X.fillna(0)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=7)

    print("start training...")
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    print("start prediction...")
    predicted_train = clf.predict(X_train)
    predicted_test = clf.predict(X_test)

    accuracy_train = accuracy_score(predicted_train, y_train)
    accuracy_test = accuracy_score(predicted_test, y_test)

    print("ACC TEST: " + str(accuracy_test))
    print("ACC TRAIN: " + str(accuracy_train))

    fpr, tpr, _ = metrics.roc_curve(np.array(y_train), clf.predict_proba(X_train)[:, 1])
    auc_train = metrics.auc(fpr, tpr)

    fpr, tpr, _ = metrics.roc_curve(np.array(y_test), clf.predict_proba(X_test)[:, 1])
    auc_test = metrics.auc(fpr, tpr)

    print("AUC TEST: " + str(auc_test))
    print("AUC TRAIN: " + str(auc_train))


def mlp(x_train, y_train, max_words, x_test, y_test):
    print('Building model...')
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    history = model.fit(x_train, y_train,
                        batch_size=128,
                        epochs=15,
                        verbose=1,
                        validation_split=0.1)
    score = model.evaluate(x_test, y_test,
                           batch_size=128, verbose=1)
    print('Test score:', score[0])
    print('Test accuracy:', score[1])


predict_random_forest()
