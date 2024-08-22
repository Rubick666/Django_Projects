import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("E:\Programming\Machine learning Quizes\Files\china_gdp.csv")
# print (df.head())


# plt.figure(figsize=(8, 5))
x_data, y_data = (df["Year"].values, df["Value"].values)
# plt.plot(x_data, y_data, 'ro')
# plt.xlabel("Year")
# plt.ylabel("GDP")
# plt.show()


def sigmoid(x, Beta_1, Beta_2):
    y = 1 / (1 + np.exp(-Beta_1 * (x - Beta_2)))
    return y

Beta_1 = 690.4517118227653
Beta_2 = 0.9972071272524615
y_pred = sigmoid(x_data, Beta_1, Beta_2)
# plt.plot(x_data, y_pred*15000000000000.0)
# plt.plot(x_data, y_data, 'ro')
# plt.show()


# Let's normalize our data
xdata = x_data / max(x_data)
ydata = y_data / max(y_data)
print (max(y_data))


# Finding the best parameters for our fitting !
from scipy.optimize import curve_fit
popt, pcov = curve_fit(sigmoid, xdata, ydata)
print (f"Beta_1 = {popt[0]} , Beta_2 = {popt[1]}")


x = np.linspace(1960, 2015, 55)
x = x/max(x)
plt.figure(figsize=(8, 5))
y = sigmoid(x, *popt)
plt.plot(xdata, ydata, 'ro', label="data")
plt.plot(x, y, linewidth=3.0, label = "fit")
plt.ylabel("GDP")
plt.xlabel("Year")
print (sigmoid((2011/2015), *popt)*10354831729340.4)
plt.show()
