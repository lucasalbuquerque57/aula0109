import pandas as pd
import json

credits = pd.read_csv("tmdb_5000_credits.csv", header=0)
print(credits.head())
print(credits[['title','cast']])


cast = credits['cast'].apply(json.loads).tolist()
title = credits['title'].tolist()

for x in range(len(title)):
    movie = cast[x]
    i = 0
    auxString = "Filme: " + title[x] + " - Ator:"

    for actor in cast[x]:
        i += 1
        if(i < 3 ):
            auxString += " " + actor['name'] + " | "
        else:
            break

    print(auxString.rstrip(" |"))