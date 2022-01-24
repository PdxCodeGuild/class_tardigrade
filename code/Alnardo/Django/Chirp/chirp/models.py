from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=20)
    chirp = models.CharField(max_length=150)

    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='chirps')

    def __str__(self):
        return self.title
    

