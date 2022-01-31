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

class checkout(models.Model):
    book = models.ForeignKey('book',       on_delete=models.CASCADE)
    user = models.CharField(max_length=200)
    checkout = models.BooleanField(auto_created= False)
    timestamp = models.DateTimeField(null=True, blank=True)


# book: the book that the user checked out or checked in
# user: a text field containing the name of the user that checked out or checked in the book
# checkout: a boolean indicating whether the book was checked out or checked in
# timestamp: a datetime that records when the book was checked out or in
    



    
    def __str__(self):
        return self.name