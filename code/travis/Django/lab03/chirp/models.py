from django.db import models
from django.contrib.auth.models import User



class Chirp(models.Model):
    title = models.CharField(max_length= 15)
    message = models.CharField(max_length=128)

    post_date = models.DateField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


    def __str__(self):

        return self.title




