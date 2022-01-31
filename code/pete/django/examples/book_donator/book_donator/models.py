from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    author =  models.ForeignKey(Author, on_delete=models.PROTECT, related_name='books')
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    pages = models.IntegerField()

    def __str__(self):
        return self.title

# class Deer(models.Model):
#     class Meta:
#         verbose_plural_name = 'deer' # shows up as 'deer' instead of 'deers' in the admin panel
#     antlers = models.IntegerField()