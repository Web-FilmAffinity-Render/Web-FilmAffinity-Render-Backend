from django.db import models

class review(models.Model):

    movie_title = models.CharField(max_length=100)
    user_username = models.EmailField()
    review_text = models.TextField()
    review_rate = models.FloatField(max_length=4)
