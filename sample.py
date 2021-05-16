import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn import preprocessing
from sklearn.cluster import KMeans

#data 
data = pd.read_csv('data.csv')
stockUnits = data['StockCode']

columns_to_keep = ['UnitPrice','Quantity']
dataSet = data.loc[:,columns_to_keep]
x = dataSet['UnitPrice']
y = dataSet['Quantity']

x_arr = x.values.reshape(-1,1)
y_arr = y.values.reshape(-1,1)
# print(y_arr[:10])

#scaling
scalerx = preprocessing.StandardScaler().fit(x_arr)
x_scaled = scalerx.transform(x_arr) 

scalery = preprocessing.StandardScaler().fit(y_arr)
y_scaled = scalery.transform(y_arr) 
# print(y_scaled[:10])

# plt.scatter(x_scaled,y_scaled)
# plt.show()


#Kmeans 
kmeans = KMeans(n_clusters=3) #3 classes
y_kmeans = kmeans.fit_predict(dataSet) 

plt.scatter(x, y, c=y_kmeans, cmap='viridis')
centers = kmeans.cluster_centers_
print(centers)

# [[1.58771429e+00 8.53651071e+03]
#  [3.84629895e+00 6.98449526e+02]
#  [1.60181818e+00 4.46432727e+04]]



# plt.scatter(centers[:,0], centers[:,1], c='red', alpha=0.5) 
# plt.show()

clusters_assigned = kmeans.labels_
# print(clusters_assigned[:10]) [2 1 2 2 2 2 1 2 1 0]

# dataSet["class"] = clusters_assigned
# dataSet.to_csv('newdata.csv')