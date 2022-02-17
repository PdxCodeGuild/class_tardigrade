from sqlite3 import Timestamp
from turtle import textinput, title
from venv import create
from django.db import models

# Create your models here.
from django.db import models



class book(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add= True)
    author = models.ForeignKey('author',       on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.author}'

class author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class checkout(models.Model):
    book = models.ForeignKey('book', on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    checkout = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return f'{self.book}  { self.checkout}  {self.timestamp} {self.user}'

# book: the book that the user checked out or checked in
# user: a text field containing the name of the user that checked out or checked in the book
# checkout: a boolean indicating whether the book was checked out or checked in
# timestamp: a datetime that records when the book was checked out or in
    



    
  