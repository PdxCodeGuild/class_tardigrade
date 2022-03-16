from django.contrib import admin

from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    fields = ['author_name']


class BookAdmin(admin.ModelAdmin):
    fields = ['title', 'publish_date', 'author_name', "is_checked_out", "user", "time_stamp" ]

#class CheckoutBookAdmin(admin.ModelAdmin):
 #   fields = ['title', 'user', 'is_checked_out', 'time_stamp']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
#admin.site.register(CheckoutBook)