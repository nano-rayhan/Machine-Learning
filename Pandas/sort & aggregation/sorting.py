import pandas as pd

data = {
    "Name" : ['ashik','Rayhan','Sahed','Robin','Niran'],
    "Age" : [22, 23, 23 ,22, 21],
    "Salary" : [1000,4000,1400,1500,2000],
    "City" : ['Horankhola', 'Shibpur', 'Horonkhola', 'Kadirchar', 'Brajerkandi']
}

df = pd.DataFrame(data)

print(df)

# df.sort_values(by = 'Age', ascending=False, inplace=True)
# print(df)

#multiple column sort
df.sort_values(by= ['Age', 'Salary'], ascending=[True, False],inplace=True)
print(df)

avg_salary = df['Salary'].mean()
print(avg_salary)