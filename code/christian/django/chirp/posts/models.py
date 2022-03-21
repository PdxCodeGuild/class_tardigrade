from django.db import models
from django.utils import timezone
from datetime import date
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User

#Tweet Post model

class Posts(models.Model):
    title = models.CharField(max_length=200)     
    body = models.CharField(max_length= 500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.title},{self.user},{self.body}'
    
    def get_absolute_url(self):
        return reverse("posts_detail", kwargs={"pk": self.pk}) #return detail post 
    
    
    
    


# Create your models here.
