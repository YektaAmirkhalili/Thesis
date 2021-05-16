import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

d1 = pd.read_csv("clustering.py")
d2 = pd.read_csv("final.csv")

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

