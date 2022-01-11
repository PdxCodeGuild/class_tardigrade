from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=2)
    slug = models.SlugField()

    def __str__(self):
        return self.abbreviation

class Person(models.Model):
    name = models.CharField(max_length=50)
    # many-to-one relationship 
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='people')

    def __str__(self):
        return self.name