from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='AP')
    def __str__(self):
        return self.name
    
    @property
    def nameorder(self):
        return self.author.all().order_by('title')

class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True, related_name='author')
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Checkout(models.Model):
    book = models.ForeignKey('Book', on_delete=models.PROTECT, related_name='checkout')
    user = models.CharField(max_length=75)
    checkout = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.book.title
