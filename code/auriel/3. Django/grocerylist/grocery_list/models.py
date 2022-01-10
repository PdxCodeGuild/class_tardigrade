from django.db import models

class GroceryItem(models.Model):
    description = models.CharField(max_length=100)
    created_date = models.DateField
    completed_date = models.DateField
    completed = models.BooleanField
