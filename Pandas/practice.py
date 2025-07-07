import pandas as pd

df = pd.read_csv("product_sales_data.csv")

max_units = df['UnitsSold'].max()

top_selling =df[df['UnitsSold']  == max_units]
# print(top_selling)

# print(df.groupby('Category')['Price'].mean())

print(df[df['Stock'] < 50])

# df['TotalRevenue'] = df['Price'] * df['UnitsSold']

print(df)

print(df.sort_values(by='Price', ascending=False))






# # print(df[df["Price"] > 20000])
# # print(df[df["Category"] == "Accessories"])

# #create a new columns
# x = df['Salary_Thoussands'] = df['Price'] / 1000

# y = df.groupby('Category')['Price'].mean()
# print(y)
# z = df['ProductName'].value_counts()
# # print(z)
# # print(df.sort_values(by='Price',ascending=False))
# # print(df.duplicated().sum())
# print(df['ProductName'].unique())