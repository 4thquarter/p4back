from rest_framework import generics
from .serializers import ArtistSerializer, ArtworkSerializer
from .models import Artist, Artwork, ArtistImage, ArtworkImage
from django_filters.rest_framework import DjangoFilterBackend


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email']
    search_fields = ['name', 'email', 'information']


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtworkList(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'artist',
                        'primary_pallet', 'secondary_pallet', 'medium']
    search_fields = ['title', 'artist', 'description']


class ArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
