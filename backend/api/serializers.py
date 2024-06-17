from .models import CustomUser
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id","email","password","phone","location","username"]
        extra_kwargs = {"password": {"write_only": True}}

    def create (self,validated_data):
         user = CustomUser.objects.create_user(**validated_data) 
         return user  