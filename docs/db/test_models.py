from django.test import TestCase
from django.contrib.auth.models import User
from datetime import timedelta, datetime
from models import Book, Film, Autor, Regie, Genre, Language, UserBorrowed, UserReserved, UserReview

class MediaModelTest(TestCase):

    def setUp(self):
    
        # Add Languages
        languages = ["Englisch", "Spanisch", "Französisch", "Deutsch", "Italienisch", "Chinesisch", "Japanisch"]
        for language in languages:
            Language.objects.create(name=language)

        # Add Genres
        genres = ["Fiktion", "Thriller", "Romantik", "Science-Fiction", "Fantasy", "Mystery", "Biografie", "Komödie", "Drama"]
        for genre in genres:
            Genre.objects.create(name=genre)

        # Add Users
        users = [
            {"username": "user1", "password": "password1"},
            {"username": "user2", "password": "password2"},
        ]

        for user in users:
            User.objects.create_user(**user)

        # Add Authors
        authors = ["Andy Weir", "J.K. Rowling", "Haruki Murakami", "Agatha Christie", "George Orwell"]
        for author in authors:
            Autor.objects.create(name=author)

        # Add Directors
        directors = ["Christopher Nolan", "Quentin Tarantino", "Steven Spielberg", "Hayao Miyazaki", "Martin Scorsese"]
        for director in directors:
            Regie.objects.create(name=director)

        # Add Book
        book_data = {
            "title": "Der Marsianer",
            "author": Autor.objects.get(name="Andy Weir"),
            "description": "Eine Überlebensgeschichte für das 21. Jahrhundert und der internationale Bestseller.",
            "cover_image": "Der_Marsianer.jpg",
            "genre": Genre.objects.get(name="Science-Fiction"),
            "language": Language.objects.get(name="Englisch"),
            "release_year": 2011,
            "ISBN": "978-0-8041-3902-1",
            "borrowed": False,
            "reserved": False,
            "media_type": "book",
        }
        Book.objects.create(**book_data)

        # Add Film
        film_data = {
            "title": "May December",
            "regie": Regie.objects.get(name="Hayao Miyazaki"),
            "description": "Middle aged Gracie lives a happy, well settled life with her husband.",
            "cover_image": "May_December.jpg",
            "genre": Genre.objects.get(name="Komödie"),
            "language": Language.objects.get(name="Englisch"),
            "release_year": 2023,
            "FSK": 16,
            "IMDb": 7.1,
            "borrowed": False,
            "reserved": False,
            "media_type": "film",
        }
        Film.objects.create(**film_data)

    def test_user_borrowed_book(self):
        user1 = User.objects.get(username="user1")
        book = Book.objects.get(title="Der Marsianer")

        user_borrowed_data = {
            "user": user1,
            "media": book,
            "return_date": datetime.now().date() + timedelta(weeks=2),
        }
        UserBorrowed.objects.create(**user_borrowed_data)

        user_borrowed_instance = UserBorrowed.objects.get(user=user1, media=book)

        self.assertEqual(user_borrowed_instance.user, user1)
        self.assertEqual(user_borrowed_instance.media, book)
        self.assertEqual(user_borrowed_instance.return_date, datetime.now().date() + timedelta(weeks=2))

    def test_user_reserved_film(self):
        user1 = User.objects.get(username="user1")
        film = Film.objects.get(title="May December")

        user_reserved_data = {
            "user": user1,
            "media": film,
            "reserved_till": datetime.now().date() + timedelta(weeks=2),
        }
        UserReserved.objects.create(**user_reserved_data)

        user_reserved_instance = UserReserved.objects.get(user=user1, media=film)

        self.assertEqual(user_reserved_instance.user, user1)
        self.assertEqual(user_reserved_instance.media, film)
        self.assertEqual(user_reserved_instance.reserved_till, datetime.now().date() + timedelta(weeks=2))

    def test_user_review_book(self):
        user2 = User.objects.get(username="user2")
        book = Book.objects.get(title="Der Marsianer")

        user_review_data = {
            "user": user2,
            "media": book,
            "rating": 5,
            "review_text": "Absolutely great",
        }
        UserReview.objects.create(**user_review_data)

        user_review_instance = UserReview.objects.get(user=user2, media=book)

        self.assertEqual(user_review_instance.user, user2)
        self.assertEqual(user_review_instance.media, book)
        self.assertEqual(user_review_instance.rating, 5)
        self.assertEqual(user_review_instance.review_text, "Absolutely great")
