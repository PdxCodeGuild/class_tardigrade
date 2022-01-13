from django.db import models



class Author(models.Model):

    author_name = models.CharField(max_length=30)
  #  books_written = models.CharField(max_length=30)

    def __str__(self):
        return self.author_name





class Book(models.Model):
    title = models.CharField(max_length=30)
    publish_date = models.CharField(max_length=30)    
    author_name = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

