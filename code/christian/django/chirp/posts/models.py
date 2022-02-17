from django.db import models
from django.utils import timezone

class Twerp(models.Model):
    body = models.CharField(max_length= 128)
    posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.body


# Create your models here.
