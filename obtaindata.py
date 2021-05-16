#load data 
import pandas as pd

dataset = pd.read_excel('dataset.xlsx', index_col=0);
pd.set_option('display.max_columns', None) #show all columns when printing df
# print(dataset.head())

#seperate data based on product codes --- group by totalBuys 
data_prices_grouped = dataset.groupby(["StockCode", "Description"], as_index=False)["UnitPrice"].median() #get median prices 
# print(data_prices_grouped.head())

data_quantities_grouped = dataset.groupby(["StockCode", "Description"], as_index=False)["Quantity"].sum() #get sum of all quantities regardless of price 
# print(data_quantities_grouped.head())

#join the two databases 
# ds_join = data_prices_grouped.join(data_quantities_grouped.set_index('StockCode'), on='StockCode')
# ds_join = pd.concat([data_prices_grouped, data_quantities_grouped], ignore_index=True)
ds_join = data_prices_grouped.merge(data_quantities_grouped, how='inner', on='StockCode')
# print(ds_join.head())


# #calculate total value of products = totalBuys * unitPrice 
ds_join["totalValue"] = ds_join["Quantity"] * ds_join["UnitPrice"]
# print(ds_join.head())

#save dataset to a file 
ds_join.to_csv('data.csv', index=False)

# dataset_new["totalValue"] = dataset_new["Quantity"] * dataset_new["UnitPrice"]
# # print(dataset_new.head())

# #another groupby for products with different dates and prices, using median of total value
# dataset_final = dataset_new.groupby(["StockCode", "Description"], as_index=False)["totalValue"].median();
# print(dataset_final.head())



