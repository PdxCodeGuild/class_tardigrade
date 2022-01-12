from django.db import models
from django.db.models.fields import BooleanField

class book:
    title=models.CharField(max_length=50),
    publish_date=models.DateField
    author=models.CharField(max_length=25)
    slug = models.SlugField()

def __str__(self):
    return self.title     
class author:
    first_last_name=models.CharField(max_length=25),
    books=models.models.ForeignKey(book)

def __str__(self):
    return self.first_last_name


class checked_out:
    checked_out=models.BooleanField(default=True)
    checkout_time=models.DateTimeField()
    



    