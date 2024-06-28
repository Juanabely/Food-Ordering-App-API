from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Food(models.Model):
    food_name = models.CharField(max_length=50)
    image_url = models.URLField()
    detail = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.food_name

class Orders(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    

    def __str__(self):
        return f"order for {self.user.username}: {self.food.food_name}"
