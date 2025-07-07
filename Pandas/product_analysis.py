import pandas as pd
df = pd.read_csv("products-100.csv")


# print(df.info())

# print(df.describe())

# print(df[df['Stock'] < 100])
# x = df['Category'].value_counts().head()
# x = df.groupby('Brand')['Price'].mean()
x = df['Currency'].unique()
df['StockValue'] = df['Price'] * df['Stock']

print(df['StockValue'].sort_values( ascending=False).head(5))
print(df.isnull().sum())