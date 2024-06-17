from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    phone=models.CharField(max_length=20,blank=True,null=True)
    location = models.CharField(max_length=255)
    def __str__(self):
        return self.email
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')