from django.test import TestCase
from django.urls import reverse
from .models import Movie

class MovieDeleteViewTest(TestCase):
    
    def setUp(self):
        self.movie = Movie.objects.create(title="V wie Vendetta", director="James McTeigue") 

    def test_get_method(self):
        response = self.client.get(reverse('movie-delete', kwargs={'pk': self.movie.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_confirm_delete.html')

    def test_post_method(self):
        response = self.client.post(reverse('movie-delete', kwargs={'pk': self.movie.pk}))
        self.assertEqual(response.status_code, 302)  # 302 is the status code for a successful redirect
        self.assertFalse(Movie.objects.filter(pk=self.movie.pk).exists())  # Ensure the movie has been deleted