from django.contrib import admin

# Register your models here.
from django.contrib import admin
from matplotlib.style import library
from .models import author, book

admin.site.register(author)
admin.site.register( book)