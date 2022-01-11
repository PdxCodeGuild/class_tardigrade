from django.db import models

# Create your models here.
class Item(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True, editable=True)
    completed_date = models.DateField(max_length=10, null=True, blank=True)
    completed = models.BooleanField(default=False)

#add dunder method

    def __str__(self):
        return self.description