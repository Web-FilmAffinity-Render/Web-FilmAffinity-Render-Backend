from django.contrib import admin
from project.movies import models

@admin.register(models.Movie)
class Movie_Admin(admin.ModelAdmin):
    pass