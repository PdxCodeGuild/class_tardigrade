from django.db import models

class State(models.Model):
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=2)