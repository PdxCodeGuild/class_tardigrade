from django.contrib import admin

from .models import Book, Author, Check_Out

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Check_Out)

