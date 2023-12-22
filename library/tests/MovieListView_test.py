import pytest
from django.urls import reverse
from django.test import RequestFactory
# Hier MovieView importieren !

#Test of Data from Movie can be outputed
def test_if_data_of_movie_is_outputed_correctly():
    #Arrange
    test_object = MovieView()
    request = RequestFactory().get(reverse('movie-info'))
    #Act
    response = movie_view.get_info(request)
    
    #Assert
    assert response.status_code = 200
    assert 'Expected Data' in response.content.decode('utf-8')
