
class MovieListView:
    def get_movies(self):
        movies = [
            {"title": "Movie A", "genre": "Action"},
            {"title": "Movie B", "genre": "Comedy"},
            {"title": "Movie C", "genre": "Drama"},
            {"title": "Movie D", "genre": "Action"}
        ]
        return movies

    def sort_alphabetically(self, movies):
        sorted_movies = sorted(movies, key=lambda x: x["title"])
        return sorted_movies

    def sort_genre(self, movies, selected_genre):
        sorted_movies = [movie for movie in movies if movie["genre"] == selected_genre]
        return sorted_movies