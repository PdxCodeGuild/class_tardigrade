from django.db import models 
from django.contrib.auth.models import User

class chirp(models.Model):
    class Meta:
        verbose_name_plural = 'chirps'
    body = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.body} || {self.date}'