from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.utils import timezone
from datetime import timedelta
# Create your models here.

def return_date_time():
    now = timezone.now()
    return now + timedelta(days=14)


class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    publish_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=PROTECT, related_name='books')
    # checked_out = models.BooleanField(default=False)
    # return_date = models.DateField(default=return_date_time)

    def __str__(self):
        return f'{self.title} by {self.author}'

class Check_Out(models.Model):
    book = models.ForeignKey(Book, on_delete=PROTECT, related_name='check_outs')
    user = models.CharField(max_length=50)
    checked_out = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.title