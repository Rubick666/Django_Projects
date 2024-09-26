import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

df = pd.read_csv("E:\\Programming\\Machine learning Quizes\\Files\\cell_samples.csv")
# print (df.head())
# df["Class"].hist()
# plt.show()

# print (df["BareNuc"].value_counts())

df = df[pd.to_numeric(df["BareNuc"], errors='coerce').notnull()]
df["BareNuc"] = df["BareNuc"].astype("Int64")
# print (df.dtypes)

X = np.asarray(df[["Clump", "UnifSize", "UnifShape", "MargAdh", "SingEpiSize", "BareNuc", "NormNucl", "Mit"]])
# print (X[0:5])
Y = np.asarray(df["Class"]).astype('int')
# print (Y[0:5])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=4)

from sklearn import svm
clf = svm.SVC(kernel='rbf')
clf.fit(X_train, Y_train)
Y_hat = clf.predict(X_test)
# print (Y_hat[0:5])
# print (Y_test[0:5])

from sklearn.metrics import f1_score, jaccard_score
print (f1_score(Y_test, Y_hat, average='weighted'))
print (jaccard_score(Y_test, Y_hat, pos_label=2))
