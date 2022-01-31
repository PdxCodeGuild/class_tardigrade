from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.PROTECT, related_name='books', null=True, blank=True)
    title = models.CharField(max_length=100)
    publish_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title

class Checkout(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.PROTECT, related_name='checkouts')
    user = models.CharField(max_length=50)
    checkout = models.BooleanField(default=False)
    time = models.DateTimeField('checkout time', auto_now=True)
    def __str__(self):
        return self.book.title