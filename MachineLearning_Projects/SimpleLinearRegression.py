import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("E:\Programming\Machine learning Quizes\Files\FuelConsumption.csv")
print (df.describe())

cdf = df[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB", "CO2EMISSIONS"]]

viz = cdf[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB", "CO2EMISSIONS"]]



msk = np.random.rand(len(cdf)) < 0.8
train = cdf[msk]
test = cdf[~msk]




from sklearn import linear_model
reg = linear_model.LinearRegression()
train_x = np.asanyarray(train[["ENGINESIZE"]])
train_y = np.asanyarray(train[["CO2EMISSIONS"]])
reg.fit(train_x, train_y)

# print ("Coefficient: ", reg.coef_)
# print ("Interception: ", reg.intercept_)


plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS, color="green")
plt.plot(train_x, reg.coef_[0][0] * train_x + reg.intercept_[0], '-r')
# plt.show()


from sklearn.metrics import r2_score

test_x = np.asanyarray(test[["ENGINESIZE"]])
test_y = np.asanyarray(test[["CO2EMISSIONS"]])
test_y_ = reg.predict(test_x)
print ("R2 Score is : ", r2_score(test_y, test_y_))

