from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=50)
    completed = models.BooleanField(default=False) # todo = Todo(text='review django') # no need to set completed to False with default value
    # completed = models.BooleanField() # todo = Todo(text='review django', completed=False)

    def __str__(self):
        return f'{self.text} - completed: {self.completed}'