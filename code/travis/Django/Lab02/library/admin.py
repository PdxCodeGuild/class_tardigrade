from django.contrib import admin

from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    fields = ['author_name']


class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'publish_date', 'author_name', 'is_checked_out']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)