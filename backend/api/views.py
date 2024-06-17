from django.shortcuts import render
# views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated ,AllowAny
from django.http import JsonResponse
from rest_framework.response import Response
import requests
# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    
    def get_token(cls, CustomUser):
        token = super().get_token(CustomUser)

        # Add custom claims
        token['username'] = CustomUser.username
        token['email'] = CustomUser.email
        token['location'] = CustomUser.location
        token['phone'] = CustomUser.phone
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
  