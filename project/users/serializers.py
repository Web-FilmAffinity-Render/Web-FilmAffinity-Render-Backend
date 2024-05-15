import re
from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from project.users import models

PASSWORD_PATTERN = r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z]).*$"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["name", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        if re.fullmatch(PASSWORD_PATTERN, value):
            return value
        else:
            raise exceptions.ValidationError("Invalid password format")

    def create(self, validated_data):
        username = validated_data.get("username", validated_data["email"])
        return models.User.objects.create_user(
            username=username, **validated_data
        )

    # def update(self, instance, validated_data):
    #    if (validated_data.get('password')):
    #        instance.set_password(validated_data.pop('password'))
    #    return super().update(instance, validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)

    def validate(self, data):
        user = authenticate(username=data["email"], password=data["password"])
        if user:
            return user
        else:
            raise exceptions.AuthenticationFailed(
                f"No username {data['email']} with that password"
            )
