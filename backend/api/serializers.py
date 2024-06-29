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

class FoodItemSerializer(serializers.Serializer):
    food_name = serializers.CharField(max_length=50)
    food_price = serializers.DecimalField(max_digits=10, decimal_places=2)

class OrderSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    user_location = serializers.CharField(source='user.location', read_only=True)  # Assuming 'location' is a field in your User model
    user_phone = serializers.CharField(source='user.phone', read_only=True)  # Assuming 'phone' is a field in your User model

    class Meta:
        model = Orders
        fields = ['user', 'food_items', 'user_username', 'user_location', 'user_phone']