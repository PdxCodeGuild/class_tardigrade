from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=50)
    # one-to-many ForeignKey
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='people')
    # many-to-many ManyToManyField
    favorite_colors = models.ManyToManyField(Color)
    def __str__(self):
        return self.name

