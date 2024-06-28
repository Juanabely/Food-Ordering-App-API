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
class Food(models.Model):
    food_name = models.CharField(max_length=50)
    image_url = models.URLField()
    detail = models.TextField()
    price = models.IntegerField()    

    def __str__(self) :
        return self.food_name
    
class Order(models.Model):
    user =models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    def __str__(self) :
        return f"order for {self.user.username}:{self.food.food_name}:{self.user.location}"    