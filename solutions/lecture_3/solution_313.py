"""Open text file and read all lines into a list."""

my_movies = []
with open("movies.txt", "r") as movies:
    for movie in movies:
        my_movies.append(movie)

print(my_movies)
