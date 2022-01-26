from django.db import models


# Create your models here.
class Item(models.Model):
    description = models.CharField(max_length=150)
    completed_date = models.DateTimeField()
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return {self.description}





