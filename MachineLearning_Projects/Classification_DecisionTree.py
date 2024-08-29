import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


df = pd.read_csv("E:\\Programming\\Machine learning Quizes\\Files\\drug200.csv")
# print (df.shape)
# print(df.head())
# print (df[0:5])


X = df[["Age", "Sex", "BP", "Cholesterol", "Na_to_K"]].values
# print (X[0:5])
Y = df["Drug"].values
# print (Y[0:5])


from sklearn import preprocessing
le_sex = preprocessing.LabelEncoder()
le_sex.fit(['F', 'M'])
X[:,1] = le_sex.transform(X[:,1])

le_BP = preprocessing.LabelEncoder()
le_BP.fit(["LOW", "NORMAL", "HIGH"])
X[:, 2] = le_BP.transform(X[:, 2])

le_Cholesterol = preprocessing.LabelEncoder()
le_Cholesterol.fit(["NORMAL", "HIGH"])
X[:, 3] = le_Cholesterol.transform(X[:, 3])
# print (X[0:5])


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=3)
drugTree = DecisionTreeClassifier(criterion="entropy", max_depth = 4)
drugTree.fit(X_train, Y_train)
predTree = drugTree.predict(X_test)
# print (Y_test[0:10])
# print (predTree[0:10])


from sklearn import metrics
print ("Decision Tree's Accuracy: ", metrics.accuracy_score(Y_test, predTree))