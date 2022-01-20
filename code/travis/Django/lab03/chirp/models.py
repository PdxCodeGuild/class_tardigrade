from django.db import models





class User(models.Model):    
    user_name = models.CharField(max_length=200)





class Chirp(models.Model):
    email_address = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)



