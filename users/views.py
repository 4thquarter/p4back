from .models import User
from .serializers import UserSerializer
from django.views.generic import CreateView
from rest_framework import generics, permissions
from users.permissions import IsOwner


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]
