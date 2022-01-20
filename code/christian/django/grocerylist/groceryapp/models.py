from django.db import models

class GroceryItem(models.Model):
    text = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    
    def __str__(self):
        return self.text



# text description, a created date, a completed date, 
# and a boolean representing whether it was completed

# Create your models here.
