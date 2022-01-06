from django.db import models

class Entry(models.Model):
    class Meta:
        verbose_name_plural = 'entries'
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} || {self.date}'