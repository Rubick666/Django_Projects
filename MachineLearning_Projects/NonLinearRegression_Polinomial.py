import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv("E:\Programming\Machine learning Quizes\Files\FuelConsumption.csv")
# df.head()
# print (df.describe())


cdf = df[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB", "CO2EMISSIONS"]]
# cdf.head()


# plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color="blue")
# plt.xlabel("Engine Size")
# plt.ylabel("CO2 Emission")
# plt.show()

msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]


from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

train_x = np.asanyarray(train[["ENGINESIZE"]])
train_y = np.asanyarray(train[["CO2EMISSIONS"]])

test_x = np.asanyarray(test[["ENGINESIZE"]])
test_y = np.asanyarray(test[["CO2EMISSIONS"]])

poly = PolynomialFeatures(degree=2)
train_x_poly = poly.fit_transform(train_x)
# print (train_x_poly)


nlr = linear_model.LinearRegression()
nlr.fit(train_x_poly, train_y)
print ("Coefficients: ", nlr.coef_)
print ("Intercept: ", nlr.intercept_)


plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color="blue")
XX = np.arange(0.0, 10.0, 0.1)
YY = nlr.intercept_[0] + nlr.coef_[0][1]*XX + nlr.coef_[0][2] * np.power(XX, 2)
plt.plot(XX, YY, '-r')
plt.xlabel("Engine Size")
plt.ylabel("Emission")
# plt.show()


from sklearn.metrics import r2_score
test_X_poly = poly.fit_transform(test_x)
test_y_ = nlr.predict(test_X_poly)
print ("R2-score is: ", r2_score(test_y, test_y_))


# If we wanted to use degree = 3 ...
'''
.
.
.
poly = PolynomialFeatures(degree=3)
train_x_poly = poly.fit_transform(train_x)
# print (train_x_poly)


nlr = linear_model.LinearRegression()
nlr.fit(train_x_poly, train_y)
print ("Coefficients: ", nlr.coef_)
print ("Intercept: ", nlr.intercept_)


plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color="blue")
XX = np.arange(0.0, 10.0, 0.1)
YY = nlr.intercept_[0] + nlr.coef_[0][1]*XX + nlr.coef_[0][2] * np.power(XX, 2) + nlr.coef_[0][3] * np.power(XX, 3)
plt.plot(XX, YY, '-r')
plt.xlabel("Engine Size")
plt.ylabel("Emission")
plt.show()


from sklearn.metrics import r2_score
test_X_poly = poly.fit_transform(test_x)
test_y_ = nlr.predict(test_X_poly)
print ("R2-score is: ", r2_score(test_y, test_y_))
'''
# the reult is worse rather than better