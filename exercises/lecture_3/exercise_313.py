"""Open text file and read all lines into a list."""

my_movies = []
movies = open("movies.txt", "r", encoding="utf-8")
for movie in movies:
    my_movies.append(movie)
movies.close()
