from django.test import TestCase
from lib_app.models import Media, Book, Movie, Author, Director, Genre, Language, UserBorrowed, UserReserved, UserReview
from django.contrib.auth import get_user_model


class MediaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name='Fantasy')
        Language.objects.create(name='English')

    def test_title_label(self):
        media = Media.objects.create(title='Test Media', media_type='book', genre=Genre.objects.get(id=1), language=Language.objects.get(id=1), description='Test Description', release_year=2022)
        field_label = media._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_genre_relationship(self):
        genre = Genre.objects.create(name='Horror')
        media = Media.objects.create(title='Test Media', media_type='book', genre=genre, language=Language.objects.get(id=1), description='Test Description', release_year=2022)
        self.assertEqual(media.genre, genre)

    def test_language_relationship(self):
        language = Language.objects.create(name='German')
        media = Media.objects.create(title='Test Media', media_type='book', genre=Genre.objects.get(id=1), language=language, description='Test Description', release_year=2022)
        self.assertEqual(media.language, language)


class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Test Author')
        Genre.objects.create(name='Fantasy')
        Language.objects.create(name='English')

    def test_author_relationship(self):
        author = Author.objects.get(id=1)
        book = Book.objects.create(title='Test Book', media_type='book', genre=Genre.objects.get(id=1), language=Language.objects.get(id=1), description='Test Description', release_year=2022, author=author, ISBN='1234567890')
        self.assertEqual(book.author, author)

    def test_isbn_label(self):
        book = Book.objects.create(title='Test Book', media_type='book', genre=Genre.objects.get(id=1), language=Language.objects.get(id=1), description='Test Description', release_year=2022, author=Author.objects.get(id=1), ISBN='1234567890')
        field_label = book._meta.get_field('ISBN').verbose_name
        self.assertEqual(field_label, 'ISBN')


class MovieModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Director.objects.create(name='Test Director')
        Genre.objects.create(name='Fantasy')
        Language.objects.create(name='English')

    def test_director_relationship(self):
        director = Director.objects.get(id=1)
        movie = Movie.objects.create(title='Test Movie', media_type='movie', genre=Genre.objects.get(id=1), language=Language.objects.get(id=1), description='Test Description', release_year=2022, director=director, FSK=12, IMDb=7.5)
        self.assertEqual(movie.director, director)

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Author.objects.create(name='Big Bob')

    def test_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

User = get_user_model()

class UserBorrowedModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='testuser')
        test_genre = Genre.objects.create(name='Test Genre')
        test_language = Language.objects.create(name='Test Language')
        test_media = Media.objects.create(title='Test Media', media_type='book', genre=test_genre, language=test_language, description='Test Description', release_year=2022)
        UserBorrowed.objects.create(user=test_user, media=test_media, return_date='2024-04-05')

    def test_user_relationship(self):
        borrowed_item = UserBorrowed.objects.get(id=1)
        self.assertEqual(borrowed_item.user.username, 'testuser')

    def test_media_relationship(self):
        borrowed_item = UserBorrowed.objects.get(id=1)
        self.assertEqual(borrowed_item.media.title, 'Test Media')

    def test_return_date_label(self):
        borrowed_item = UserBorrowed.objects.get(id=1)
        field_label = borrowed_item._meta.get_field('return_date').verbose_name
        self.assertEqual(field_label, 'return date')


class UserReservedModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='testuser')
        test_genre = Genre.objects.create(name='Test Genre')
        test_language = Language.objects.create(name='Test Language')
        test_media = Media.objects.create(title='Test Media', media_type='book', genre=test_genre, language=test_language, description='Test Description', release_year=2022)
        UserReserved.objects.create(user=test_user, media=test_media, reserved_till='2024-04-05')

    def test_user_relationship(self):
        reserved_item = UserReserved.objects.get(id=1)
        self.assertEqual(reserved_item.user.username, 'testuser')

    def test_media_relationship(self):
        reserved_item = UserReserved.objects.get(id=1)
        self.assertEqual(reserved_item.media.title, 'Test Media')

    def test_reserved_till_label(self):
        reserved_item = UserReserved.objects.get(id=1)
        field_label = reserved_item._meta.get_field('reserved_till').verbose_name
        self.assertEqual(field_label, 'reserved till')


class UserReviewModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create(username='testuser')
        test_genre = Genre.objects.create(name='Test Genre')
        test_language = Language.objects.create(name='Test Language')
        test_media = Media.objects.create(title='Test Media', media_type='book', genre=test_genre, language=test_language, description='Test Description', release_year=2022)
        UserReview.objects.create(user=test_user, media=test_media, rating=5, review_text='Great book!')

    def test_user_relationship(self):
        review = UserReview.objects.get(id=1)
        self.assertEqual(review.user.username, 'testuser')

    def test_media_relationship(self):
        review = UserReview.objects.get(id=1)
        self.assertEqual(review.media.title, 'Test Media')

    def test_rating_label(self):
        review = UserReview.objects.get(id=1)
        field_label = review._meta.get_field('rating').verbose_name
        self.assertEqual(field_label, 'rating')
