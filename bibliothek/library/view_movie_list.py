import sqlite3



class MovieListView:
    def get_movies(self):
        conn = sqlite3.connect('Artikel.db')  
        cursor = conn.cursor()
        cursor.execute("SELECT Name, Genre FROM Artikel")
        movies = [{"title": row[0], "genre": row[1]} for row in cursor.fetchall()]
        conn.close()
        return movies
        

    def sort_alphabetically(self, movies):
        sorted_movies = sorted(movies, key=lambda x: x["title"])
        return sorted_movies

    def sort_genre(self, movies, selected_genre):
        sorted_movies = [movie for movie in movies if movie["genre"] == selected_genre]
        return sorted_movies