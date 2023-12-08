from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    locked = models.BooleanField(default=False)


class Media(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self): return self.title
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    media_type = models.CharField(choices=MediaType.choices, max_length=10)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='media_covers/', null=True, blank=True)
    release_year = models.IntegerField()
    borrowed = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)


class MediaType(models.TextChoices):
    BOOK = 'BOOK', 'Buch'
    FILM = 'FILM', 'Film'
    GAME = 'GAME', 'Spiel'


class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name


class Autor(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name


class UserBorrowed(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    return_date = models.DateField()


class UserReserved(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    reserved_till = models.DateTimeField()


class UserReview(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()

