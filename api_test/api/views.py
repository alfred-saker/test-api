from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegistrationView(APIView):
    def post(self, request):
        data = {
            "email": "alfredkuate55@gmail.com",
            "password1": "password@1234",
            "password2": "password@1234"
        }

        response = requests.post('http://hire-game.netsach.dev/api/v1.1/auth/register/', data=data)
        
        if response.status_code == status.HTTP_201_CREATED:
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Registration failed'}, status=status.HTTP_400_BAD_REQUEST)

