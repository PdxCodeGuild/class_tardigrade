from django.db import models
from django.db.models.fields import BooleanField
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publish_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True, related_name='author')
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Checked(models.Model):
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book')
    username = models.CharField(max_length=50, null=True, blank=True)
    check_out_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    checked_out = models.BooleanField(default=True)
    def __str__(self):
        return self.username
