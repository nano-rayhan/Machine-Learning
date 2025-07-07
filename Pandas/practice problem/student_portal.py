import pandas as pd

df = pd.read_csv("student_marks_english.csv")

avg = df.groupby("Student")['Marks'].mean().reset_index()
top_student = avg.loc[avg["Marks"].idxmax()]

print(top_student)
print()
avg_sub = df.groupby('Subject')['Marks'].mean().reset_index()
less_avg_sub = avg_sub.loc[avg_sub['Marks'].idxmin()]
print(less_avg_sub)

print()

print(df[df['Marks'] < 82])

print()
max_num = df.loc[df.groupby("Subject")['Marks'].idxmax()]

print(max_num[["Subject", "Student", "Marks"]])