from .models import CustomUser,Food,Orders
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","email","password","phone","location","username"]
        extra_kwargs = {"password": {"write_only": True}}

    def create (self,validated_data):
         user = CustomUser.objects.create_user(**validated_data) 
         return user  
    
class FoodSerializer (serializers.ModelSerializer):
    class Meta:
        model = Food
        fields  = '__all__'

class OrderSerializer (serializers.ModelSerializer):
    class Meta :
        model = Orders
        fields = '__all__'
        extra_kwargs = {"user":{"write_only":True}}