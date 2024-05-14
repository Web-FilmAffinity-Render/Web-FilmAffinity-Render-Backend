from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from project.movies.models import Movie
from .models import Review
from project.users.models import User
from .serializers import ReviewSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token

class ListReviewView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):

        movie_title = self.request.query_params.get('movie_title')
        queryset = Review.objects.filter(movie_title=movie_title)

        return queryset

from api.users.models import User
from rest_framework.permissions import IsAuthenticated

class CreateReviewView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        _ = self.get_logged_in_user(request)
        movie_title = request.data.get('movie_title')
        _ = self.get_movie(movie_title)
        
        return super().create(request)

    def get_logged_in_user(self, request):
        if "session" in request.COOKIES:
            user = Token.objects.get(key=request.COOKIES.get("session")).user
            return User.objects.get(username=user)
        else:
            raise ObjectDoesNotExist("User not logged in.")

    def get_movie(self, movie_title):
        try:
            return Movie.objects.get(title=movie_title)
        except Movie.DoesNotExist:
            raise Movie.DoesNotExist("Movie does not exist.")

    def perform_create(self, serializer):
        # Set the logged-in user as the review's user
        serializer.save(user_username=self.request.user)

    def handle_exception(self, exc):
        if isinstance(exc, ObjectDoesNotExist):
            return Response({"error": str(exc)}, status=status.HTTP_401_UNAUTHORIZED)
        elif isinstance(exc, Movie.DoesNotExist):
            return Response({"error": str(exc)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return super().handle_exception(exc)



