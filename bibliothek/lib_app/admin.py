from django.contrib import admin
from .models import Movie, Book, Author, Director, Genre, Language, UserBorrowed, UserReserved, UserReview, User

admin.site.register(Author)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Language)

class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "genre", "author", "language", "ISBN", "release_year", "borrowed", "reserved"]
    list_filter = ["borrowed", "reserved", "genre", "author", "language"]
    search_fields = ["title"]

admin.site.register(Book, BookAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "genre", "director", "language", "release_year", "borrowed", "reserved"]
    list_filter = ["borrowed", "reserved", "genre", "director", "language"]
    search_fields = ["title"]

admin.site.register(Movie, MovieAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "last_name", "first_name", "locked"]
    list_filter = ["locked"]
    search_fields = ["username", "last_name"]
admin.site.register(User, UserAdmin)

admin.site.register(UserBorrowed)
admin.site.register(UserReserved)
admin.site.register(UserReview)