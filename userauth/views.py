from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404


# Login view Below

@api_view(['POST'])
def login(request):
    # Get user by pass in username or return 404
    user = get_object_or_404(User, username=request.data['username'])

    # Check if password provided and in database match
    if not user.check_password(request.data['password']):
        return Response({"message": "Invalid Username or Password"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Get or create token
    token, created = Token.objects.get_or_create(user=user)

    # serializer data sent by user
    serializer = UserSerializer(instance=user)

    # Respond with status of 200 with Token and user data
    return Response({'Token': token.key, 'User': serializer.data})


# Signup View Below

@api_view(['POST'])
def signup(request):
    # serialize data sent by user
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        # Fetch save user by username from database and hash password
        user = User.objects.get(username=request.data.get('username'))
        user.set_password(request.data.get('password'))
        user.save()

        # Create token for user
        token = Token.objects.create(user=user)

        # Respond with status of 200 with Token and user data
        return Response({'Token': token.key, 'User': serializer.data})
    
    # Throw errors if serialization of data failed
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
