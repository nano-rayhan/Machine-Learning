import pandas as pd

df = pd.read_csv("market_sales.csv")
print()
print(df.loc[df['Quantity'].idxmax()])

daily_sales = df.groupby('Date')['Total_Price'].sum().reset_index()
top_day = daily_sales.loc[daily_sales['Total_Price'].idxmax()]
print(daily_sales)
print()
print(top_day)

print()

per_product_profit = df.groupby('Product')['Total_Price'].sum().reset_index()
print(per_product_profit)


df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Total_Price'].sum().reset_index()

print(monthly_sales)