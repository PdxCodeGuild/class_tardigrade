from django.db import models

class Emoticon(models.Model):
    emoticon = models.CharField(max_length=3)

    def __str__(self):
        return self.emoticon