from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    job = models.TextField(max_length=200, blank=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.user.username
