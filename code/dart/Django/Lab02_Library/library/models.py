# from django.db import models
# from django.db.models.deletion import PROTECT

# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return self.name

# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     publish_date = models.DateField(null=True, blank=True)
#     author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True) # a book can only have one author
#     def __str__(self):
#         return self.title

# class Checkout(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='checkouts')
#     user = models.CharField(max_length=50)
#     checked_out = models.BooleanField(default=False)
#     check_out_date_and_time = models.DateTimeField(auto_now=True)
#     check_in_date_and_time = models.DateTimeField(null=True, blank=True)
#     def __str__(self):
#         return self.book.title

# class Genre(models.Model):
#     genre = models.CharField(max_length=50)
#     book = models.ManyToManyField(Book)
#     def __str__(self):
#         return self.genre

from django.db import models
from django.db.models.fields import BooleanField
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True, related_name='author')
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Checked(models.Model):
    class Meta:
        verbose_name_plural = "checks"
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='book')
    user_name = models.CharField(max_length=50, null=True, blank=True)
    checked_out = models.BooleanField(default=False)
    out_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    def __str__(self):
        return self.user_name