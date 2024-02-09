from  django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from MovieDeleteViewClass import MovieDeleteViewClass

class MovieDeleteViewTest(TestCase):
    
    def setUp(self) -> None:
        self.movie = Movie.objects.create(title= "V wie Vendetta", director = "James McTeigue") 