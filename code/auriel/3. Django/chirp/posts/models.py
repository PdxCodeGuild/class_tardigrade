from django.db import models
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.contrib.auth.models import User


class Post(models.Model):
    chirp = models.CharField(max_length=288)
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    saved = models.BooleanField(default=False)
    saved_date = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return f'{self.author},{self.time},\n {self.chirp}'