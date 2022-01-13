from django.db import models
from django.db.models.deletion import CASCADE, PROTECT

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=PROTECT, related_name='books')
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title} by {self.author}'