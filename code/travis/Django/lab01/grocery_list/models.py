from django.db import models
from datetime import datetime




class GroceryItem(models.Model):
    description = models.CharField(max_length=20)
    created_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(null=True)
    completed = models.BooleanField(null=True)
    
    def __str__(self):
        return self.description