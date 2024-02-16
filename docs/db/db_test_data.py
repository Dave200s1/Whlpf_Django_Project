{
  "languages": [
    {"name": "Englisch"},
    {"name": "Spanisch"},
    {"name": "Französisch"},
    {"name": "Deutsch"},
    {"name": "Italienisch"},
    {"name": "Chinesisch"},
    {"name": "Japanisch"}
  ],
  "genres": [
    {"name": "Fiktion"},
    {"name": "Thriller"},
    {"name": "Romantik"},
    {"name": "Science-Fiction"},
    {"name": "Fantasy"},
    {"name": "Biografie"},
    {"name": "Komödie"}
  ],
  "users": [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"}
  ],
  "authors": [
    {"name": "Andy Weir"},
    {"name": "J.K. Rowling"},
    {"name": "Haruki Murakami"},
    {"name": "Agatha Christie"},
    {"name": "George Orwell"}
  ],
  "directors": [
    {"name": "Christopher Nolan"},
    {"name": "Quentin Tarantino"},
    {"name": "Steven Spielberg"},
    {"name": "Hayao Miyazaki"},
    {"name": "Martin Scorsese"}
  ],
  "books": [
    {
      "title": "Der Marsianer",
      "author": "Andy Weir",
      "description": "Eine Überlebensgeschichte für das 21. Jahrhundert und der internationale Bestseller.",
      "cover_image": "Der_Marsianer.jpg",
      "genre": "Science-Fiction",
      "language": "Englisch",
      "release_year": 2011,
      "ISBN": "978-0-8041-3902-1",
      "borrowed": false,
      "reserved": false,
      "media_type": "book"
    },
    {
      "title": "Harry Potter and the Philosopher's Stone",
      "author": "J.K. Rowling",
      "description": "The story of a young boy, Harry Potter, who discovers that he is a wizard and is invited to attend Hogwarts School of Witchcraft and Wizardry.",
      "cover_image": "Harry_Potter_and_the_Philosophers_Stone.jpg",
      "genre": "Fantasy",
      "language": "English",
      "release_year": 1997,
      "ISBN": "978-0-7475-3269-6",
      "borrowed": true,
      "reserved": false,
      "media_type": "book"
    },
    {
      "title": "1984",
      "author": "George Orwell",
      "description": "A dystopian novel by George Orwell.",
      "cover_image": "1984.jpg",
      "genre": "Science-Fiction",
      "language": "English",
      "release_year": 1949,
      "ISBN": "978-0-452-28423-4",
      "borrowed": false,
      "reserved": false,
      "media_type": "book"
    },
    {
      "title": "The Da Vinci Code",
      "author": "Dan Brown",
      "description": "A mystery thriller novel by Dan Brown.",
      "cover_image": "da_vinci_code.jpg",
      "genre": "Thriller",
      "language": "English",
      "release_year": 2003,
      "ISBN": "978-0-385-50420-5",
      "borrowed": false,
      "reserved": false,
      "media_type": "book"
    }
  ],
  "films": [
    {
      "title": "May December",
      "director": "Hayao Miyazaki",
      "description": "Middle aged Gracie lives a happy, well settled life with her husband.",
      "cover_image": "May_December.jpg",
      "genre": "Komödie",
      "language": "Englisch",
      "release_year": 2023,
      "FSK": 16,
      "IMDb": 7.1,
      "borrowed": false,
      "reserved": false,
      "media_type": "film"
    },
    {
      "title": "Inception",
      "director": "Christopher Nolan",
      "description": "A thief who enters the dreams of others to steal their secrets from their subconscious.",
      "cover_image": "inception.jpg",
      "genre": "Action",
      "language": "English",
      "release_year": 2010,
      "FSK": 12,
      "IMDb": 8.8,
      "borrowed": false,
      "reserved": true,
      "media_type": "film"
    },
    {
      "title": "Pulp Fiction",
      "director": "Quentin Tarantino",
      "description": "Various interrelated stories of criminals in Los Angeles.",
      "cover_image": "pulp_fiction.jpg",
      "genre": "Crime",
      "language": "English",
      "release_year": 1994,
      "FSK": 16,
      "IMDb": 8.9,
      "borrowed": true,
      "reserved": false,
      "media_type": "film"
    },
    {
      "title": "The Shawshank Redemption",
      "director": "Frank Darabont",
      "description": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
      "cover_image": "shawshank_redemption.jpg",
      "genre": "Drama",
      "language": "English",
      "release_year": 1994,
      "FSK": 12,
      "IMDb": 9.3,
      "borrowed": false,
      "reserved": false,
      "media_type": "film"
    }
  ],
  "user_borrowed": [
    {
      "user": "user1",
      "media": "Der Marsianer",
      "return_date": "2024-03-01"
    }
  ],
  "user_reserved": [
    {
      "user": "user1",
      "media": "May December",
      "reserved_till": "2024-03-01"
    }
  ],
  "user_reviews": [
    {
      "user": "user2",
      "media": "Der Marsianer",
      "rating": 5,
      "review_text": "Absolutely great"
    }
  ]
}
