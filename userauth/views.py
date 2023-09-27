from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, EmailSerializer, ResetPasswordSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from .send_email import send


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


@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()

    return Response("User successfully logged out")


# Password Reset view below

@api_view(['POST'])
def forgot_password(request):

    serializer = EmailSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    email = request.data.get('email')

    user = User.objects.filter(email=email).first()


    if user:
        encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        reset_url = reverse('reset-password', kwargs={'encoded_pk': encoded_pk,'token': token})

        reset_link = f"localhost:8000{reset_url}"

        send('Reset Password Link', reset_link, [email])

        return Response({'message': reset_link}, status=status.HTTP_200_OK)
    
    return Response({'message': 'User does not exist'})


@api_view(['PATCH'])
def reset(request, *args, **kwargs):
    serializer = ResetPasswordSerializer(data=request.data, context={"kwargs": kwargs})

    serializer.is_valid(raise_exception=True)

    return Response({'message': 'Password suceesfully updated'})






