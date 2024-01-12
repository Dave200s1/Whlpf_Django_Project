from django.db import models
from django.contrib.auth.models import AbstractUser


MEDIA_CHOICES = [('book', 'Book'), ('film', 'Film')]

class Media(models.Model):
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=20, choices=MEDIA_CHOICES)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='media_covers/', null=True, blank=True)
    release_year = models.IntegerField()
    borrowed = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)

    class Meta:
        abstract = True

class Book(Media):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Film(Media):
    regie = models.ForeignKey('Regie', on_delete=models.CASCADE)
    FSK = models.IntegerField()
    IMDb = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self): 
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    locked = models.BooleanField(default=False)
    
class Autor(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class UserBorrowed(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    return_date = models.DateField()

class UserReserved(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    reserved_till = models.DateField()

class UserReview(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()

