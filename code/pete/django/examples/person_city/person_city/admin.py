from django.contrib import admin

from .models import Person, City, Color
admin.site.register(Person)
admin.site.register(City)
admin.site.register(Color)