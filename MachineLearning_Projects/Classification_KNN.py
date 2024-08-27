import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing


df = pd.read_csv("E:\\Programming\\Machine learning Quizes\\Files\\teleCust1000t.csv")
# print (df.shape)
# print (df.head())
# print (df['custcat'].value_counts())

'''
df.hist(column="income", bins=50)
plt.show()
'''

# print (df.columns)


x = df[['region', 'tenure', 'age', 'marital', 'address', 'income', 'ed',
       'employ', 'retire', 'gender', 'reside']].values
# print (x[0:5])
y = df['custcat'].values
# print (y[0:5])


# Normalizing Data...
scaler = preprocessing.StandardScaler().fit(x)
x = scaler.transform(x.astype(float))
# print (x[0:5])


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=4)
print ("Train set: ", x_train.shape, y_train.shape)
print ("Test set: ", x_test.shape, y_test.shape)


from sklearn.neighbors import KNeighborsClassifier
'''
k = 9
neigh = KNeighborsClassifier(n_neighbors = k).fit(x_train, y_train)
print (neigh)
y_hat = neigh.predict(x_test)
print (y_hat[0:5])
print (y_test[0:5])
'''

from sklearn import metrics
# print ("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(x_train)))
# print ("Test set Accuracy: ", metrics.accuracy_score(y_test, y_hat))


Ks = 10
mean_acc = np.zeros((Ks-1))

for n in range(1, Ks):
    neigh = KNeighborsClassifier(n_neighbors = n).fit(x_train, y_train)
    y_hat = neigh.predict(x_test)
    mean_acc[n-1] = metrics.accuracy_score(y_test, y_hat)

print (mean_acc)