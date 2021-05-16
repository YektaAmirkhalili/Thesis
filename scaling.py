#here I will find two measures: Value and net difference of days bought 

import pandas as pd 
import numpy as np

data = pd.read_csv("dataWithDiff.csv")

data["Earliest_Date"] = pd.to_datetime(data["Earliest_Date"])
data["Latest_Date"] = pd.to_datetime(data["Latest_Date"])
data["new_diff"] = data["Latest_Date"] - data["Earliest_Date"]
data["new_diff"] = data["new_diff"] / np.timedelta64(1,'D')

data.to_csv("new_days_diff.csv")

# TotalQuant = data["Quantity"].sum() 
# max_diff = data["new_diff"].max()

# print(TotalQuant)
# print(max_diff)
# 5167808
# 697.0

# TotalQuant = 5167808
# max_diff = 697 

