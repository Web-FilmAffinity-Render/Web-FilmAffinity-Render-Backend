from rest_framework import serializers
from project.movies import models

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = "__all__"

    def create(self, validated_data):
      return models.Movie.objects.create_movie(title=validated_data['title'], **validated_data)

    def update(self, instance, validated_data):
       return super().update(instance, validated_data)

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = '__all__'
        
    def validate_stock(self, value):
        if value == 0:
            raise serializers.ValidationError("Stock cannot be zero")
        return value
    
    def create(self, validated_data):
        return models.Movie.objects.create(**validated_data)
