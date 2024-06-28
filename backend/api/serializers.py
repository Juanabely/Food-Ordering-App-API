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

from rest_framework import serializers
from.models import Food, Orders

class FoodItemSerializer(serializers.Serializer):
    food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all())
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()

    def validate(self, data):
        # Ensure the calculated price matches the expected price
        food_item = data['food_id']
        expected_price = food_item.price * data['quantity']
        if data['price']!= expected_price:
            raise serializers.ValidationError({"price": "Calculated price does not match expected price."})
        return data

class FoodSerializer (serializers.ModelSerializer):
    class Meta:
        model = Food
        fields  = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True)

    class Meta:
        model = Orders
        fields = ['user', 'food_items']

    def create(self, validated_data):
        food_items_data = validated_data.pop('food_items')
        order = Orders.objects.create(**validated_data)
        for food_item_data in food_items_data:
            FoodItemSerializer().create(food_item_data)
        return order
