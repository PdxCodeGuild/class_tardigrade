from django.contrib import admin
from .models import Book, Author, Check_out_in
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Check_out_in)
