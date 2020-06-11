from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('artwork/', views.ArtworkList.as_view(), name="artwork_list"),
    path('artwork/<int:pk>', views.ArtworkDetail.as_view(), name="artwork_detail"),
    path('ArtworkMedia/<int:pk>', views.ArtworkMediaDetail.as_view(),
         name='ArtworkMedia_detail'),
    path('ArtworkMedia/', views.ArtworkMediaList.as_view(),
         name='ArtworkMedia_list'),
    path('ArtistMedia/<int:pk>', views.ArtistMediaDetail.as_view(),
         name='ArtistMedia_detail'),
    path('ArtistMedia/', views.ArtistMediaList.as_view(), name='ArtistMedia_list'),
]
