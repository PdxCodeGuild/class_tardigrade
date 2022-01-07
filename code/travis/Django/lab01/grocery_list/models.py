from django.db import models
from datetime import datetime




class GroceryItem(models.Model):
    description = models.CharField(max_length=20)
    created_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.description