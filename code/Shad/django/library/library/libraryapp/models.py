from turtle import textinput, title
from venv import create
from django.db import models

# Create your models here.
from django.db import models

from numpy import integer

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