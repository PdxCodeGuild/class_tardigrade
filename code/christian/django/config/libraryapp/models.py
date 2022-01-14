from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import BooleanField
from django.utils import timezone



class Author(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=PROTECT, related_name= 'books')
    
    
    
    
    def __str__(self):
        return self.title

class Checkout(models.Model):
    book = models.ForeignKey(Book, on_delete=PROTECT, related_name= 'checkouts' )
    user = models.TextField()
    #False = book is checked out
    checkout = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.title

# Create your models here.
