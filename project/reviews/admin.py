from django.contrib import admin
from project.reviews import models

@admin.register(models.Review)
class Review_Admin(admin.ModelAdmin):
    pass
