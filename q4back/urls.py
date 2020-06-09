from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('artists', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('artwork/', views.ArtworkList.as_view(), name="artwork_list"),
    path('artwork/<int:pk>', views.ArtworkDetail.as_view(), name="artwork_detail")

]
