from django.db import models
from django.db.models.fields import BooleanField, CharField


class Author(models.Model):
    first_last_name=models.CharField(max_length=25)
    def __str__(self):
        return self.first_last_name

class Book (models.Model):
    title=models.CharField(max_length=50)
    publish_date=models.DateField()
    author=models.ForeignKey(Author, on_delete=models.PROTECT,max_length=25)
    checked_out=models.BooleanField(default=True)
    checkout_time=models.DateField(null=True, blank =True)

    def __str__(self):  
        return self.title     


    





    



    