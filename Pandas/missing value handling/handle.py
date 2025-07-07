import pandas as pd

data = {
    "Name" : ['ashik','Rayhan','Sahed',None,'Niran'],
    "Age" : [22, 23, None,22, 21],
    "City" : ['Horankhola', 'Shibpur', None, 'Kadirchar', 'Brajerkandi']

}

df = pd.DataFrame(data)

print(df)

df.dropna(inplace=True)
print(df)


