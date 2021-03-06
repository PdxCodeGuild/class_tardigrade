from django.db import models

class GroceryItem(models.Model):

    item = models.CharField(max_length=100)
    created_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item