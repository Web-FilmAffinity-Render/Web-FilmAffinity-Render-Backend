import re
from rest_framework import serializers, exceptions
from django.contrib.auth import authenticate
from api.users import models

PASSWORD_PATTERN = r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z]).*$"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        if re.fullmatch(PASSWORD_PATTERN, value):
            return value
        else:
            raise exceptions.ValidationError("Invalid password format")

    def create(self, validated_data):
        return models.Usuario.objects.create_user(
            username=validated_data["email"], **validated_data
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
