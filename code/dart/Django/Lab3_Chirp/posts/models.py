from django.db import models

class User_Info(models.Model):
    user_name = models.CharField(max_length=24)
    user_image = models.URLField()
    user_bio = models.CharField(max_length=300)
    def __str__(self):
        return self.user_name

class Post(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=128)
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User_Info, on_delete=models.CASCADE, related_name='user')
    def __str__(self):
        post_name = f"{self.title} by {self.user}"
        return post_name