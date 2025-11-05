import pandas as pd
import numpy as np

ariseism_product_data = pd.read_json("/Users/shinena/dev/Taobao-vs-Western-Fashion-Brands/ariseism_products.json")

np.random.seed(0)

#print(ariseism_product_data.head())

missing_values_count = ariseism_product_data.isnull().sum()
#print(missing_values_count[0:10])

ariseism_product_data.dropna()
print(ariseism_product_data.shape)