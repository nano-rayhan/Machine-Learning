import pandas as pd

df = pd.read_csv("product_sales_data.csv")

print(df)

print()

df["PriceHike"] = df['Price'] * 0.1

print(df)

# df.insert(2, "PriceHikee", df['Price']*.1)
# print(df)
#updating value
df.loc[2, "Price"] = 5000
print(df)

#remove value
df.drop(columns= 'PriceHike', inplace=True)
print(df)