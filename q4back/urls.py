from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth import views as auth_views
from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('artwork/', views.ArtworkList.as_view(), name="artwork_list"),
    path('artwork/<int:pk>', views.ArtworkDetail.as_view(), name="artwork_detail"),
    path('artworkmedia/<int:pk>', views.ArtworkMediaDetail.as_view(),
         name='artworkmedia_detail'),
    path('artworkmedia/', views.ArtworkMediaList.as_view(),
         name='artworkmedia_list'),
    path('artistmedia/<int:pk>', views.ArtistMediaDetail.as_view(),
         name='artistmedia_detail'),
    path('artistmedia/', views.ArtistMediaList.as_view(),
         name='artistmedia_list'),
]
