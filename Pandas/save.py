import pandas as pd

data = {
    "Name" : ['Rayhan','Sahed','Faysal','Niran'],
    "Age" : [23,22,21,22],
    "City" : ['Narsingdi','Shibpur','Dulalpur','Horankhola']
}

df = pd.DataFrame(data)
print(df)
# df.to_csv("information.csv", index=False)
df.to_excel("information.xlsx", index=False)
# df.to_json("information.json", index=False)