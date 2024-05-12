from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    duration = models.CharField(max_length=10)
    rating = models.FloatField()
    votes = models.IntegerField()
    image = models.CharField(max_length=100)
    plot = models.TextField()
    trailer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
