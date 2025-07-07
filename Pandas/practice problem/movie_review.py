import pandas as pd

df = pd.read_csv("movie_ratings.csv")

most_movie_users = df['User'].value_counts().idxmax()
print(most_movie_users)

mean_rating = df.groupby('Movie')['Rating'].mean().idxmax()
print(mean_rating)

High_Rating = df[df['Rating']>4]['Movie'].unique()
print(High_Rating)