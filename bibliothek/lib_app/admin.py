from django.contrib import admin
from .models import Movie, Book, Author, Director, Genre, Language, UserBorrowed, UserReserved, UserReview, User

admin.site.register(Book)
admin.site.register(Movie)
admin.site.register(Author)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(UserBorrowed)
admin.site.register(UserReserved)
admin.site.register(UserReview)

class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "last_name", "first_name", "locked"]

admin.site.register(User, UserAdmin)