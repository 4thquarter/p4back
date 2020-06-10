from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/new', views.ArtistNew.as_view(), name='artist_new'),
    path('artists/filter', views.ArtistFilter.as_view(), name='artist_filter'),
    path('artists/search', views.ArtistSearch.as_view(), name='artist_search'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('artists/edit/<int:pk>', views.ArtistEdit.as_view(), name='artist_edit'),
    path('artwork/', views.ArtworkList.as_view(), name="artwork_list"),
    path('artwork/new', views.ArtworkNew.as_view(), name="artwork_new"),
    path('artwork/filter', views.ArtworkFilter.as_view(), name="artwork_filter"),
    path('artwork/search', views.ArtworkSearch.as_view(), name="artwork_search"),
    path('artwork/<int:pk>', views.ArtworkDetail.as_view(), name="artwork_detail"),
    path('artwork/edit/<int:pk>', views.ArtworkEdit.as_view(), name='artwork_edit'),
    path('artworkimage/<int:pk>', views.ArtworkImageDetail.as_view(), name='artworkimage_detail'),
    path('artworkimage/', views.ArtworkImageList.as_view(), name='artworkimage_list'),
]
