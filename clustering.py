# number of clusters; A, B, and C === n_clusters = 3
# number of initializations; n_init (default 10)
# maximum number of iterations for minimizing inertia; max_iter (default 300)
# tolerance for convergence; tol 

#imports 
import numpy as np 
import pandas as pd
import os, time 
import matplotlib.pyplot as plt 
import seaborn as sns 
color = sns.color_palette()
import matplotlib as mpl 
from sklearn import preprocessing as pp 
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve, average_precision_score
from sklearn.metrics import roc_curve, auc, roc_auc_score 
from sklearn.cluster import KMeans 
from scipy.cluster.hierarchy import dendrogram, cophenet, fcluster
from scipy.spatial.distance import pdist

#data 
data = pd.read_csv('data.csv')
columns_to_keep = ['StockCode','totalValue']
dataSet = data.loc[:,columns_to_keep]
# print(dataSet.head())

plt.plot(dataSet['StockCode'], dataSet['totalValue']);
plt.show()

from numpy import unique
from numpy import where

# #variable setting 
# n_clusters = 3
# n_init = 10 
# max_iter = 300
# tol = 0.0001
# random_state = 43
# n_jobs = 2



# kmeans = KMeans(n_clusters)
# KMeans.fit(X)








