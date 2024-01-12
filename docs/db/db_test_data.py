from django.contrib.auth.models import User
from datetime import datetime, timedelta
from models import Media, Book, Film, Genre, Language, CustomUser, Autor, Regie, UserBorrowed, UserReserved, UserReview

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
book = Book.objects.create(**book_data)

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
film = Film.objects.create(**film_data)

# Add UserBorrowed
user_borrowed_data = {
    "user": User.objects.get(username="user1"),
    "media": Book.objects.get(title="Der Marsianer"),
    "return_date": datetime.now().date() + timedelta(weeks=2),
}
UserBorrowed.objects.create(**user_borrowed_data)

# Add UserReserved
user_reserved_data = {
    "user": User.objects.get(username="user1"),
    "media": Film.objects.get(title="May December"),
    "reserved_till": datetime.now().date() + timedelta(weeks=2),
}
UserReserved.objects.create(**user_reserved_data)

# Add UserReview
user_review_data = {
    "user": User.objects.get(username="user2"),
    "media": Book.objects.get(title="Der Marsianer"),
    "rating": 5,
    "review_text": "Absolutely great",
}
UserReview.objects.create(**user_review_data)
