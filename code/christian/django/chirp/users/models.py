from calendar import c
from django.db import models

class Create(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


# Create your models here.
