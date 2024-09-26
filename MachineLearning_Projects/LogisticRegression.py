import pandas as pd
import numpy as np
import scipy.optimize as opt
from sklearn import preprocessing
import matplotlib.pyplot as plt

df = pd.read_csv("E:\\Programming\\Machine learning Quizes\\Files\\ChurnData.csv")
# print (df.head())

df = df[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip', 'callcard', 'wireless', 'churn']]
df['churn'] = df["churn"].astype(int)
# print (df.head())

X = np.asarray(df[['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip']])
Y = np.asarray(df['churn'])
# print (X[0:5])
# print (Y[0:5])

X = preprocessing.StandardScaler().fit(X).transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test , Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=4)
# print ("Train set: ", X_train.shape, Y_train.shape)
# print ("Test_set: ", X_test.shape, Y_test.shape)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
LR = LogisticRegression(C=0.01, solver="liblinear").fit(X_train, Y_train)
LR

Y_hat = LR.predict(X_test)
# print (Y_hat)
# print (Y_test)
Y_hat_proba = LR.predict_proba(X_test)
# print (Y_hat_proba)

from sklearn.metrics import jaccard_score
# print (jaccard_score(Y_test, Y_hat, pos_label=0))

from sklearn.metrics import log_loss
# print (log_loss(Y_test, Y_hat_proba))