from django.db import models
    
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    types = models.ManyToManyField('Type')
    sprite = models.URLField()

class Type(models.Model):
    type = models.CharField(max_length=50)