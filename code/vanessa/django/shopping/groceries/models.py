from django.db import models

# Create your models here.
class Item(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(max_length=10)
    completed_date = models.DateField(max_length=10, null=True, blank=True)
    completed = models.BooleanField

#add dunder method

    def __str__(self):
        return self.description