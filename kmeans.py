import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn import preprocessing
from sklearn.cluster import KMeans

# print(pd.__version__) version 23
#data 
data = pd.read_csv('data.csv')

columns_to_keep = ['StockCode','totalValue']
dataSet = data.loc[:,columns_to_keep]
x = dataSet['StockCode']
y = dataSet['totalValue']

y_arr = y.values.reshape(-1,1)
# print(y_arr[:10])

#scaling
scaler = preprocessing.StandardScaler().fit(y_arr)
y_scaled = scaler.transform(y_arr) 
# print(y_scaled[:10])

# plt.scatter(x,y_scaled)
# plt.show()

#Kmeans 
kmeans = KMeans(n_clusters=3) #3 classes
kmeans.fit(dataSet)
y_kmeans = kmeans.predict(dataSet) 

plt.scatter(x, y_scaled, c=y_kmeans, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c='red', alpha=0.5) 
plt.show()



# print(dataSet.head())
# X = dataSet['StockCode']
# y = dataSet['totalValue']
# y_n = np.array(y).reshape(-1,1) 

# trans = preprocessing.MinMaxScaler()
# transformed_data = trans.fit_transform(dataset_arr['totalValue'])

# # scaler = preprocessing.StandardScaler() 
# # scaled_ds = scaler.fit_transform(y_n)
# # print(y_n)

# plt.scatter(transformed_data['StockCode'], transformed_data['totalValue'])
# plt.show()
# X = scaled_ds['StockCode']
# y = scaled_ds['totalValue'] 

# plt.scatter(X,y) 
# plt.show()

# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
# X_validation, y_validation = 

