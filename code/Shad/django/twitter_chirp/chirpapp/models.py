from django.db import models



class post(models.Model):
    myfield = models.CharField(max_length=128)
    myfield = models.TextField

    
    def __str__(self):
        return self.myfield
# Create your models here.
