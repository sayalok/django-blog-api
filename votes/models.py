from django.db import models

from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Vote(models.Model):
	voter = models.ForeignKey(User, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
