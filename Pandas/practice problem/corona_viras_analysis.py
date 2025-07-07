import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("covid_data.csv")
most_interfec_country = df.loc[df['Infected'].idxmax(), 'Country']
print(most_interfec_country)

df['Recovery_Rate'] = round(((df['Recovered'] / df['Infected']) * 100), 2)
print(df[['Country' , 'Recovery_Rate']])

df['Death_Rate'] = round(((df['Deaths']/df['Infected']) * 100), 2)

print(df[['Country','Death_Rate']])

total_infected = df['Infected'].sum()
print("Total Infected in the world", total_infected)

plt.scatter(df['Country'],df['Infected'] ,color= 'black', marker='o', label='Corona Infected')
plt.scatter(df['Country'],df['Recovered'] ,color= 'green', marker='o', label='Corona Recovered')
plt.scatter(df['Country'],df['Deaths'] ,color= 'red', marker='o', label='Corona Deaths')

plt.legend()
plt.grid()
plt.show()