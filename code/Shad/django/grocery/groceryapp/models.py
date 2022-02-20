from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields import BooleanField

class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    

    
    
    def __str__(self):
        return self.description 