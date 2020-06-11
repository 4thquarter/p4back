from rest_framework import serializers
from django.contrib.auth.hashers import make_password  # Add this
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name']
        validate_password = make_password  # Add this
