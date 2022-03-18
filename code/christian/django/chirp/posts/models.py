from django.db import models
from django.utils import timezone
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User

class Twerp(models.Model):
    body = models.CharField(max_length= 250)
    posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.body},{self.user}'


# Create your models here.
