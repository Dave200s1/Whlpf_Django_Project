from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from lib_app.models import Film  
from datetime import timedelta

class MovieCreateViewClassTestCase(TestCase):
    
    def setUp(self):
        self.film = Film.objects.create(title="Interstellar", director="Christopher Nolan", FSK=12, IMDb=8.6)
        
    def test_create_movie_view(self):
        # Arrange
        title = "Interstellar"
        release_date = timezone.now().date() - timedelta(days=365)
        director = "Christopher Nolan"
        FSK = 12
        IMDb = 8.6
        
        # Act
        response = self.client.post(reverse('film-create'), {'title': title, 'release_date': release_date, 'director': director, 'FSK': FSK, 'IMDb': IMDb})
        
        # Assert
        self.assertEqual(response.status_code, 302)  # Assuming the view redirects after successful creation
        self.assertTrue(Film.objects.filter(title=title, release_date=release_date, director=director, FSK=FSK, IMDb=IMDb).exists())

