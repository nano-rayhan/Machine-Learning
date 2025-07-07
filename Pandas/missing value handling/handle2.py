import pandas as pd

data = {
    "Name" : ['ashik','Rayhan','Sahed',None,'Niran'],
    "Age" : [22, 23, None,22, 21],
    "City" : ['Horankhola', 'Shibpur', None, 'Kadirchar', 'Brajerkandi']

}

df = pd.DataFrame(data)

print(df)

# df.fillna(0, inplace=True)
# print(df)

#fill with calculate value
# df['Age'].fillna(df['Age'].mean() , inplace=True)
# print(df)

df['Age'] = df['Age'].interpolate(method='linear')
print(df)