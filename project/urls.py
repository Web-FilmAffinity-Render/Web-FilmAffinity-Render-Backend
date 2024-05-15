from django.contrib import admin
from django.urls import path
from project.users import views as user_views
from project.reviews import views as reviews_views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("users/signin", user_views.SigninView.as_view()),
    path("users/login", user_views.LoginView.as_view()),
    path("users/me", user_views.UserView.as_view()),
    path("users/logout", user_views.LogoutView.as_view()),

    path("reviews/", reviews_views.ListReviewView.as_view()),
    path("reviews/new", reviews_views.CreateReviewView.as_view())
]
