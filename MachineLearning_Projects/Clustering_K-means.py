import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets._samples_generator import make_blobs

df = pd.read_csv("E:\\Programming\\Machine learning Quizes\\Files\\Cust_Segmentation.csv")
# print (df.head())

df = df.drop('Address', axis=1)
# print (df.head())

from sklearn.preprocessing import StandardScaler
X = df.values[:, 1:]
X = np.nan_to_num(X)
Clus_dataset = StandardScaler().fit_transform(X)
# print (Clus_dataset)

ClusterNum = 3
k_means = KMeans(init="k-means++", n_clusters=ClusterNum, n_init=12)
k_means.fit(X)
labels = k_means.labels_
# print (labels)

df["Clus_km"] = labels
# print (df.head())

df.groupby("Clus_km").mean()
# print (df.groupby("Clus_km").mean())

area = np.pi * (X[:, 1])** 2
plt.scatter(X[:, 0], X[:, 3], s = area, c=labels.astype(np.float64), alpha=0.5)
plt.xlabel('Age', fontsize = 18)
plt.ylabel('Income', fontsize = 16)
plt.show()