import sqlite3

class MovieListView:


    def get_connection(self):
        try:
            conn = sqlite3.connect('Artikel.db')
            return conn
        except sqlite3.Error as e:
            print("Error connecting to the database:", e)
            return None

    def get_movies(self):
        conn = self.get_connection()
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

    def extract_day_from_database(self):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT ErscheinungsDatum FROM Artikel")
            date_string = cursor.fetchone()[0]
            day_substring = date_string[:2]
            conn.close()
            return day_substring
        except sqlite3.Error as e:
            print("Error accessing database:", e)

    def extract_month_from_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ErscheinungsDatum FROM Artikel")
        date_string = cursor.fetchone()[0]
        month_substring = date_string[3:5]
        conn.close()
        return month_substring

    def extract_year_from_database(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT ErscheinungsDatum FROM Artikel")
        date_string = cursor.fetchone()[0]
        year_substring = date_string[6:]
        conn.close()
        return year_substring

# Test code
if __name__ == "__main__":
    movie_list_view = MovieListView()
    print(movie_list_view.extract_year_from_database())