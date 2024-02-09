from  django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from MovieUpdateViewClass import MovieUpdateViewClass

class MovieUpdateViewTest(TestCase):
    
    def setUp(self) -> None:
        self.movie = Movie.objects.create(title= "Test Movie", director = "Michael Bay")
        
    
    @classmethod
    #expired date
    def test_update_form_date_field_label(self):
        #Arrange
        testobject = MovieUpdateViewClass() 
        #Act
        
        result = testobject.check_if_expired(testobject.getDate())
        #Assert
        self.assertFalse(result)
        
    # Test the get method of the MovieUpdateView
    def test_get_method(self):
        response = self.client.get(reverse('movie-update', kwargs={'pk': self.movie.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_update.html')
    
    # Test the post method of the MovieUpdateView
    def test_post_method(self):
        updated_title = 'Updated Movie'
        updated_director = 'Updated Director'
        response = self.client.post(reverse('movie-update', kwargs={'pk': self.movie.pk}), {'title': updated_title, 'director': updated_director})
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a successful redirect
        self.movie.refresh_from_db()  # Refresh the movie instance from the database
        self.assertEqual(self.movie.title, updated_title)
        self.assertEqual(self.movie.director, updated_director)
        
    
   