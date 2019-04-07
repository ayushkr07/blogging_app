from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    text=models.TextField()
    published_date=models.DateTimeField(default=timezone.now)
