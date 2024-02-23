from django.test import TestCase
from django.urls import reverse
from lib_app.models import Film
from django.contrib.auth.models import User

class MovieCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        test_user = User.objects.create_user(username='testuser', password='12345')

    def test_movie_create_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='12345')

        # Access the movie creation view
        response = self.client.get(reverse('movie-create'))

        # Check that the view returns a 200 status code
        self.assertEqual(response.status_code, 200)

        # Create a movie using the view
        response = self.client.post(reverse('movie-create'), {
            'title': 'Test Movie',
            'director': 'Test Director',
            'FSK': 12,
            'IMDb': 7.5,
            'genre': 'Test Genre',
            'language': 'Test Language',
            'description': 'Test Description',
            'cover_image': 'test_image.jpg',
            'release_year': 2022
        })

        # Check that the movie is created successfully
        self.assertEqual(response.status_code, 302)  # Assuming a successful creation redirects to another page

        # Optionally, you can further test the created movie's details and attributes
        created_movie = Film.objects.get(title='Test Movie')
        self.assertEqual(created_movie.director, 'Test Director')
        # Add more assertions as needed
