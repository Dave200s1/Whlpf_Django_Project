from django.shortcuts import render
from django.views import generic
from .models import Author, Book, Movie
from django.views.generic import ListView, DetailView


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
    