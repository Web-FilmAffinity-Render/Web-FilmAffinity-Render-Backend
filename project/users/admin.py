from django.contrib import admin
from project.users import models

@admin.register(models.User)
class User_Admin(admin.ModelAdmin):
    pass