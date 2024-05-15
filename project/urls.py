from django.contrib import admin
from django.urls import path
from project.users import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("users/signin", views.SigninView.as_view()),
    path("users/login", views.LoginView.as_view()),
    path("users/me", views.UserView.as_view()),
    path("users/logout", views.LogoutView.as_view())
]
