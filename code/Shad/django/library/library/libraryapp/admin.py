from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import author, book, checkout

admin.site.register(author)
admin.site.register( book)
admin.site.register( checkout)