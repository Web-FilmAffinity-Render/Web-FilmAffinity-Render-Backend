from rest_framework import serializers
from project.reviews import models

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ["movie_title", "user_username", "review_text", "review_rate"]

    def create(self, validated_data):
      
        return models.Review.objects.create(
            **validated_data
        )