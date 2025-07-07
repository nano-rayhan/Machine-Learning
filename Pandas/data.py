import pandas as pd

df = pd.read_csv("machine-readable-business-employment-data-dec-2024-quarter.csv")
# print(df.describe())
print(df.shape)
print(df.columns)
# print(df.info())
# print("Display the first 10 data")
# print(df.head(10))