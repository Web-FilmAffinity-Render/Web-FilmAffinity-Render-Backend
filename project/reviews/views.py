from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from project.movies.models import Movie
from project.reviews.models import Review
from project.users.models import User
from project.reviews.serializers import ReviewSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError

class ListReviewView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        movie_title = self.request.query_params.get('movie_title')

        if not movie_title:
            raise ValidationError("The 'movie_title' query parameter is required.")

        try:
            movie = Movie.objects.get(title=movie_title)
            queryset = Review.objects.filter(movie_title=movie)
        except ObjectDoesNotExist:
            queryset = Review.objects.none()

        return queryset

    def handle_exception(self, exc):
        
        if isinstance(exc, ValidationError):
            return Response({"error": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().handle_exception(exc)

class CreateReviewView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def create(self, request):
        self.get_logged_user(request)
        movie_title = request.data.get('movie_title')
        self.get_movie(movie_title)
        
        return super().create(request)          

    def get_logged_user(self, request):
        """
        Checks the User is logged and the user_username exists
        """
        
        if "session" in request.COOKIES:
            user = Token.objects.get(key=request.COOKIES.get("session")).user
            if user:
                try:
                    User.objects.get(username=request.data.get('user_username'))
                except User.DoesNotExist:
                    raise User.DoesNotExist(f"No user {request.data.get('user_username')}")
        else:
            raise ObjectDoesNotExist("User not logged in.")

    def get_movie(self, movie_title):
        try:
            Movie.objects.get(title=movie_title)
        except Movie.DoesNotExist:
            raise Movie.DoesNotExist("Movie does not exist.")

    def handle_exception(self, exc):
        if isinstance(exc, ObjectDoesNotExist):
            return Response({"error": str(exc)}, status=status.HTTP_401_UNAUTHORIZED)
        elif isinstance(exc, Movie.DoesNotExist):
            return Response({"error": str(exc)}, status=status.HTTP_404_NOT_FOUND)
        else:
            return super().handle_exception(exc)



