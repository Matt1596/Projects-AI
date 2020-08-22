from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

np.set_printoptions(threshold=np.nan)

iris = load_iris()
X = iris.data
y = iris.target

#print(X)


df = pd.read_csv('CC GENERAL.csv')

print(df.shape)



xDf = df[df.columns[1:17]]     ### DE LA COLUMNA 1 (excluyendo el ID) A LA ANTEULITMA
yDf = df.values[:,17]    ###TOMAMOS LA COLUMNA 17 (TENURE) COMO LA CLASE DEL DATASET

##Queremos solo los valores:
X = xDf.values[:17]
Y = yDf
X = X.astype('int64')

#X = df[df.columns[0:17][2:5] ]
#Y = df[df.columns[17:18]]

#y = Y.astype('float64')
#X = np.round(X)
#Y = np.round(Y)

print(X)
print(Y)

k1 = KMeans(n_clusters=6).fit(X)

print("K1 Labels:" , k1.labels_)

##CENTROS:

print ("K1 Centroids:", k1.cluster_centers_)

## Muchas variables para plotear en 3d.

