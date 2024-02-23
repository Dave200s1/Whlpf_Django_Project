from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from myapp.models import Movie  # Replace 'myapp' with the actual name of your app
from datetime import timedelta

from MovieCreateViewClass import MovieCreateViewClass

class MovieCreateViewClass (TestCase):
    
    def setup() -> None:
        self.movie = Movie.object.create(title = "Intersteller", director = "Chrstipher Nolan")
        
        
    @classmethod
    def test_create_movie_view(self):
        #Arrange
        title = "Intersteller"
        release_date = timezone.now().date() - timedelta(days=365)
        
        director = "Crhistopher Nolan"
        movie = Movie.objects.create(title=title, release_date=release_date, director=director)
        #Act
        response = self.client.post(reverse('movie-create'), {'title': title, 'release_date': release_date, 'director': director})
        
        #Assert
        self.assertEqual(response.status_code, 302)  # Assuming the view redirects after successful creation
        
        self.assertTrue(Movie.objects.filter(title=title, release_date=release_date, director=director).exists())

