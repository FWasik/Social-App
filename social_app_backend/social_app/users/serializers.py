from django.contrib.auth import get_user_model
from rest_framework import serializers as rest_serializers
from djoser import serializers

CustomUser = get_user_model()


class CustomUserCreateSerializer(serializers.UserCreateSerializer):
    middle_name = rest_serializers.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ("id", "email", "first_name", "middle_name", "last_name")


class CustomUserSerializer(serializers.UserSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "first_name", "middle_name", "last_name")


