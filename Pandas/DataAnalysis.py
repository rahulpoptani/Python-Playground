from numpy import piecewise
import pandas as pd

movies = pd.read_csv('~/Downloads/movie.csv')

director = movies.director_name
fb_likes = movies.actor_1_facebook_likes

# print(fb_likes.isna().sum())


# print(fb_likes.head())

print(movies.filter(items = ['Jon']))