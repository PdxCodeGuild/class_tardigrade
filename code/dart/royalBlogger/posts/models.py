from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    class Meta:
        ordering = ['-created_on']

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='users')
    title = models.CharField(max_length=200, unique=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    post = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        ordering = ['created_on']

    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    def __str__(self):
        return '{} -- {}'.format(self.body, self.name)

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title