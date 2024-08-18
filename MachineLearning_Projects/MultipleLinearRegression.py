import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import linear_model


df = pd.read_csv("E:\Programming\Machine learning Quizes\Files\FuelConsumption.csv")
# df.describe()

cdf = df[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_CITY", "FUELCONSUMPTION_HWY", "FUELCONSUMPTION_COMB", "CO2EMISSIONS"]]
# print (cdf.head())

plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color="blue")
plt.xlabel("Engine Size")
plt.ylabel("Co2 Emission")
#plt.show()


msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

# plt.scatter(train.ENGINESIZE, test.CO2EMISSIONS, color="red")
# plt.xlabel("Engine Size")
# plt.ylabel("Co2 Emission")


reg = linear_model.LinearRegression()
train_X = np.asanyarray(train[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]])
train_y = np.asanyarray(train[["CO2EMISSIONS"]])
reg.fit(train_X, train_y)
print ("Coefficients: ", reg.coef_)
print ("Intercept: ", reg.intercept_)


test_X = np.asanyarray(test[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]])
test_y = np.asanyarray(test[["CO2EMISSIONS"]])
test_y_ = reg.predict(test[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]])
print ("Variance score is: ", reg.score(test_X, test_y))

# plt.plot(train_X[:, 0], reg.coef_[0][0] * train_X[:, 0] + reg.coef_[0][1]*train_X[:, 1] + reg.coef_[0][2]*train_X[:, 2] + reg.intercept_[0], '.-r')
# plt.show()