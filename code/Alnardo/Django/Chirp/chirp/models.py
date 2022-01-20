from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=20)
    text = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    

