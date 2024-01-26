from  django.test import TestCase
from MovieListView import MovieListViewClass


class MovieListViewTest(TestCase):
    
    def test_get_movies(self):
        #Arrange
        test_object = MovieListViewTest()
        #Act
        #movies = test_object.get_moview()
        movies = [
            {"title": "Movie A", "genre": "Action"},
            {"title": "Movie B", "genre": "Comedy"},
            {"title": "Movie C", "genre": "Drama"},
            {"title": "Movie D", "genre": "Action"}
        ]
        #Assert
        self.assertEqual(len((movies)),3)
        self.assertEqual(movies[0].title, "Movie A")
        self.assertEqual(movies[1].title,"Movie B")
        self.assertEqual(movies[2].title,"Movie C")
        
        
    def test_sort_movies_aphabetically(self):
        #Arrange
        test_object = MovieListViewTest()
        #Act
        result = test_object.sort_alpahbetically()
        movies = [
            {"title": "Movie A", "genre": "Action"},
            {"title": "Movie B", "genre": "Comedy"},
            {"title": "Movie C", "genre": "Drama"},
            {"title": "Movie D", "genre": "Action"}
        ]
        #Assert
        self.assertEqual(sorted_movies[0]["title"], "Movie A")
        self.assertEqual(sorted_movies[1]["title"], "Movie B")
        self.assertEqual(sorted_movies[2]["title"], "Movie C")
        
    def test_sort_moviews_genre(self):
        #Arrange
        test_object = MovieListViewTest()
     
        result = test_object.sort_genre()
        movie_list = [
            {"title": "Movie A", "genre": "Action"},
            {"title": "Movie B", "genre": "Comedy"},
            {"title": "Movie C", "genre": "Drama"},
            {"title": "Movie D", "genre": "Action"}
        ]
        selected_genre = "Action"
        #Act
        sorted_movie_list = test_object.sort_genre(movie_list,selected_genre)
        
        #Assert
        self.assertEqual(len(sorted_movies), 2)
        self.assertEqual(sorted_movies[0]["title"], "Movie A")
        self.assertEqual(sorted_movies[1]["title"], "Movie D")