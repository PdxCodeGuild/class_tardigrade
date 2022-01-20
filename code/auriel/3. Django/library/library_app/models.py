from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True, related_name='author')
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Checkout(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    user = models.CharField(max_length=32)
    checkout = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
