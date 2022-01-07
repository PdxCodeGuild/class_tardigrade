from django.db import models

# Emoticon is the name of the model
class Emoticon(models.Model):
    # emoticon is the name of the character field, with a max length of 3 characters
    emoticon = models.CharField(max_length=3)

    def __str__(self):
        return self.emoticon