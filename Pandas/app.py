import pandas as pd

#read data from cvs file
df = pd.read_csv("C:\\Users\\user\\Desktop\\Python\\Pandas\\machine-readable-business-employment-data-dec-2024-quarter.csv", encoding="utf-8") #latin1
print(df)