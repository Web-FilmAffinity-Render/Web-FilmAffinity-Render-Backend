from django.contrib import admin
from movies import models

@admin.register(models.Movie)
class Movie_Admin(admin.ModelAdmin):
    pass