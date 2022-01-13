from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='posts')
    title = models.CharField(max_length=100)
    body = models.TextField()
    def __str__(self):
        return f'"{self.title}" by {self.author.name}'