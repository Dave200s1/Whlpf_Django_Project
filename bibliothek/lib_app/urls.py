from django.urls import path
from . import views


urlpatterns = [
#general
    path('/',views.home,name='Homepage'),
    path('/register/',views.register,name='Registrieren'),
    path('/login/',views.login,name='Anmelden'),
    path('/logout/',views.logout,name='Abmelden'),
#catalog
    path('/catalog/',views.catalog,name='Katalog'),
    path('/catalog/media',views.catalog_media,name='Medien'),
#user
    path('/users/<user_id>',views.user_id,name='Benutzerprofil'),
    path('/users/<user_id>/borrowed/',views.borrowed_media,name='Benutzer ausgeliehene Medien'),
    path('/users/<user_id>/reserved/',views.reserved_media,name='Benutzer reservierte Medien'),
    path('/users/<user_id>/recommendations/',views.recommendations,name='Empfehlungen'),
    path('/users/<user_id>/ratings/',views.rated_media,name='Benutzer-Bewertungen'),
    path('/users/<user_id>/ratings/<rating_id>/',views.ratings,name='Benutzer Bewertung Details'),
#admin
    path('/admin/users/',views.admin_user,name='Adminprofil'),
    path('/admin/users/<user_id>/',views.user_details,name='Adminprofil Details'),
    path('/admin/users/<user_id>/borrowed/',views.admin_borrowed_media,name='Admin ausgeliehene Medien'),
    path('/admin/users/<user_id>/reserved/',views.admin_reserved_media,name='Admin reservierte Medien'),
    path('/admin/users/<user_id>/ratings/',views.admin_ratings,name='Admin Bewertungen'),
    path('/admin/users/<user_id>/ratings/<rating_id>/',views.admin_rating_id,name='Admin Bewertung Details'),
#admin-media
    path('/admin/media/',views.media,name='Medien'),
    path('/admin/authors/',views.authors,name='Authoren'),
    path('/admin/regies/',views.regies,name='Regies'),
    path('/admin/genres/',views.genres,name='Genres'),
    path('/admin/ratings/',views.rating_overview,name='Bewertungen'),
    path('/admin/medias/<media_id>/',views.media_id,name='Medien Detials'),
    path('/admin/authors/<author_id>/',views.author_id,name='Author Details'),
    path('/admin/regies/<regie_id>',views.regie_id,name='Regie Details'),
    path('/admin/genre/<genre_id>',views.genre_id,name='Genre Details')
]
