from django.contrib import admin

from .models import BooksInStore, TypesOfBooks, Authors
# Register your models here.

admin.site.register(BooksInStore)
admin.site.register(TypesOfBooks)
admin.site.register(Authors)
