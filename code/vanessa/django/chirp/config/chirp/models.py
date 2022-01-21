from django.db import models

class chirp(models.Model):
    class Meta:
        verbose_name_plural = 'chirps'
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.body} || {self.date}'