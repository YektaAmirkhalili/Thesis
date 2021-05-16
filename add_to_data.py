import pandas as pd
import numpy as np


TotalQuant = 5167808
max_diff = 697 

data = pd.read_csv("new_days_diff.csv")


#add new column for value of each product 

value = price * (Quantity / TotalQuant)

#add new column for net difference of each column 

net_diff = productDiff / max_diff