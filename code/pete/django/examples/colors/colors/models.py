from django.db import models

# each Color will have a name (of the color) and a like counter

class Color(models.Model):
    color = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.color