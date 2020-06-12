from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('signup/', views.UserCreate.as_view(), name='create_user'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
]