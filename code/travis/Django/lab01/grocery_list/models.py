from django.db import models
from datetime import datetime


class GroceryItem(models.Model):
    description = models.CharField(max_length=20)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description