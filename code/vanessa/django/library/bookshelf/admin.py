from django.contrib import admin
from .models import book, author, checked_out
admin.site.register(book)
admin.site.register(author)
admin.site.register(checked_out)
