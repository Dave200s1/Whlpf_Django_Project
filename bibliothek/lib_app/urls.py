from django.urls import path
from . import views

app_name = "lib_app"

urlpatterns = [

# catalog
    path('', views.IndexView.as_view(), name='index'),

    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:book_id>/', views.BookDetailView.as_view(), name='Book'),

    path('movies', views.MovieListView.as_view(), name='Movies'),
    path('movie/<int:movie_id>/', views.MovieDetailView.as_view(), name='Movie'),

    path('authors', views.AuthorListView.as_view(), name='Authors'),
    path('author/<int:author_id>/', views.AuthorDetailView.as_view(), name='Author'),
    #Causes some issues !!!
    #path('/register/',views.register,name='Registrieren'),
    #path('/login/',views.login,name='Anmelden'),
    #path('/logout/',views.logout,name='Abmelden'),
    
    #path('/users/<user_id>',views.user_id,name='Benutzerprofil'),
    #path('/users/<user_id>/borrowed/',views.borrowed_media,name='Benutzer ausgeliehene Medien'),
    #path('/users/<user_id>/reserved/',views.reserved_media,name='Benutzer reservierte Medien'),
    #path('/users/<user_id>/recommendations/',views.recommendations,name='Empfehlungen'),
    #path('/users/<user_id>/ratings/',views.rated_media,name='Benutzer-Bewertungen'),
    #path('/users/<user_id>/ratings/<rating_id>/',views.ratings,name='Benutzer Bewertung Details'),
    
]
