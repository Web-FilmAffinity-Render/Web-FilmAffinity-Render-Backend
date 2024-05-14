from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    country = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=600)
    rate = models.CharField(max_length=10)
    genre = models.CharField(max_length=100)
    duration = models.BigIntegerField()
    # image = models.CharField(max_length=100)
    plot = models.TextField()

    def __str__(self):
        return self.title
