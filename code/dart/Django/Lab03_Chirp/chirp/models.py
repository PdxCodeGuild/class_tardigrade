from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=128)
    def __str__(self):
        return f'"{self.title}" by {self.user.name}'