from django.shortcuts import render
from django.views import generic
from .models import Author, Book, Movie
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'lib_app/index.html', {'success_message': 'Anmeldung erfolgreich!'})
        else:
            # Hinzufügen einer Fehlermeldung, wenn das Passwort falsch ist
            messages.error(request, 'Falscher Benutzername oder Passwort')
            return render(request, 'lib_app/index.html')

    return render(request, 'lib_app/index.html')


def user_logout(request):
    logout(request)
    return redirect('lib_app:index')

class IndexView(ListView):
    model = Author
    template_name = 'lib_app/index.html'
    context_object_name = 'index'

class BookListView(ListView):
    model = Book
    template_name = 'lib_app/books.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'lib_app/book.html'
    context_object_name = 'book'

class MovieListView(ListView):
    model = Movie
    template_name = 'lib_app/movies.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'lib_app/movie.html'
    context_object_name = 'movie'

class AuthorListView(ListView):
    model = Author
    template_name = 'lib_app/authors.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'lib_app/author.html'
    context_object_name = 'author'
    