from django.db import models
from django.contrib.auth.modles import User

# Create your models here.
class Items(models.model):
    user = models.ForeignKey(User, on_delete=models.cascade, null=True, blank=True)
    item = models.CharField(max_length=150)
    quantity = models.CharField(max_length=3)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']



