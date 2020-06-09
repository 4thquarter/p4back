from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('artists', views.ArtistList.as_view(), name='artist_list'),
    path('artists/filter', views.ArtistFilter.as_view(), name='artist_filter'),
    path('artists/search', views.ArtistSearch.as_view(), name='artist_search'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),

    path('artwork/', views.ArtworkList.as_view(), name="artwork_list"),
    path('artwork/filter', views.ArtworkFilter.as_view(), name="artwork_filter"),
    path('artwork/search', views.ArtworkSearch.as_view(), name="artwork_search"),
    path('artwork/<int:pk>', views.ArtworkDetail.as_view(), name="artwork_detail")

]
