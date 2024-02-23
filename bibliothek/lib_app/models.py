from django.db import models
from django.contrib.auth.models import AbstractUser
# Import the Group model from django.contrib.auth.models
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission



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


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(Media):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Film(Media):
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
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

<<<<<<< HEAD
#previous version
#class CustomUser(AbstractUser):
    #locked = models.BooleanField(default=False)
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')

class ConcreteMedia(Media):
    pass
=======

class User(AbstractUser):
    locked = models.BooleanField(default=False)
>>>>>>> 815f6870dc686b7010d770b5da94f3e2d20ebc5b


class UserBorrowed(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    media = models.ForeignKey(ConcreteMedia, on_delete=models.CASCADE)
    return_date = models.DateField()
#previous version
#class UserBorrowed(models.Model):
    #user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #media = models.ForeignKey(Media, on_delete=models.CASCADE)
    #return_date = models.DateField()


class UserReserved(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    reserved_till = models.DateField()


class UserReview(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()
