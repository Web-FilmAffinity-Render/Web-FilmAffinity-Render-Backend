from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from django.db.utils import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from project.users import serializers, models

class SigninView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def handle_exception(self, exc):
        if isinstance(exc, IntegrityError):
            return Response(status=status.HTTP_409_CONFLICT)
        else:
            return super().handle_exception(exc)
        

class LoginView(generics.CreateAPIView):
    serializer_class = serializers.LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            token, created = Token.objects.get_or_create(user=serializer.validated_data)
            response = Response(status=status.HTTP_201_CREATED)
            response.set_cookie(
                key="session",
                value=token.key,
                secure=True,
                httponly=True,
                samesite="lax",
            )
            return response
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        

class UserView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        if not "session" in self.request.COOKIES:
            raise ObjectDoesNotExist
        else:
            user = Token.objects.get(key=self.request.COOKIES.get("session")).user
            return models.User.objects.get(username=user)

    def handle_exception(self, exc):
        if isinstance(exc, ObjectDoesNotExist):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return super().handle_exception(exc)
        
class LogoutView(generics.DestroyAPIView):

    def delete(self, request):

        session_token = request.COOKIES.get("session")
        if session_token:
            # Delete the token from the database
            Token.objects.filter(key=session_token).delete()
        
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie("session")

        return response
