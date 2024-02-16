from django.contrib import admin
from .models import Media
from .models import Film
from .models import Author
from .models import Regie
from .models import Book
from .models import Genre
from .models import Language
from .models import CustomUser
from .models import UserBorrowed
from .models import UserReserved
from .models import UserReview
# Register your models here.

admin.site.register(Film)
admin.site.register(BaseException)
admin.site.register(Media)
admin.site.register(Author)
admin.site.register(Regie)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(CustomUser)
admin.site.register(UserBorrowed)
admin.site.register(UserReview)

