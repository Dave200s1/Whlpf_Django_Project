from  django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from MovieDeleteViewClass import MovieDeleteViewClass

class MovieDeleteViewTest(TestCase):
    
    def setUp(self) -> None:
        self.movie = Movie.objects.create(title= "V wie Vendetta", director = "James McTeigue") 
        
     # Test the get method of the MovieDeleteView
    def test_get_method(self):
        #Arrange/Act
        response = self.client.get(reverse('movie-delete', kwargs={'pk': self.movie.pk}))
        #Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_confirm_delete.html')
        
     # Test the post method of the MovieDeleteView
    def test_post_method(self):
        #Arrange/Act
        response = self.client.post(reverse('movie-delete', kwargs={'pk': self.movie.pk}))
        #Assert
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a successful redirect
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())  # Ensure the movie has been deleted