from django.db import models

class City(models.Model):
    class Meta: # used to make the plural name better in the admin panel (Citys vs Cities)
        verbose_name_plural = 'cities'

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name
