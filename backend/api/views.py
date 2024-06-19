import json
import logging

from django.shortcuts import render
# views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated ,AllowAny
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
@api_view(['POST'])
def index(request):
    cl = MpesaClient()
    # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
    phone_number = request.data.get('phone')
    amount = request.data.get('amount')
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)
@api_view(['POST'])
def stk_push_callback(request):
    # Log the raw request body
    logging.info(f"Raw request body: {request.body}")

    try:
        data = json.loads(request.body)
        # Continue processing...
    except json.JSONDecodeError as e:
        # Log the error for debugging
        logging.error(f"JSON decode error: {e}")
        return Response("Invalid JSON data", status=400)