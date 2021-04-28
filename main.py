import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/cwkteacher/Data/master/movie_metadata.csv')

print(df.head(5))
print(df.columns)

print(df['director_name'])

cols = ['movie_title', 'facenumber_in_poster']
print(df[cols])

# movies with imdb score > 7.5

rating = df[df['imdb_score'] > 7.5]
print(rating[['movie_title', 'imdb_score']])

country = df['country'].value_counts()
print(country.head(10))

df_gross = df.groupby('director_name')['gross'].sum()
df_gross = df_gross.sort_values(ascending=False)
print(df_gross.head(10))

df_num = df['director_name'].value_counts()
print(df_num.head(10))

df_movies_year = df.groupby(['title_year'])['movie_title'].count()
print(df_movies_year.head(50))

langs = df['language'].unique()
print(langs)