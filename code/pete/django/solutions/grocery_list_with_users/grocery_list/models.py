from django.db import models
from django.contrib.auth.models import User

class GroceryItem(models.Model):
    description = models.CharField(max_length=50)
    created_date = models.DateField(auto_now_add=True)
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='groceries')

    def __str__(self):
        return self.description