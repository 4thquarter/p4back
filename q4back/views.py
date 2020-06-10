from rest_framework import generics
from .serializers import ArtistSerializer, ArtworkSerializer
from .models import Artist, Artwork, ArtistImage, ArtworkImage
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistNew(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistFilter(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email']


class ArtistSearch(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'email', 'information']


class ArtistDetail(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtworkList(generics.ListAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class ArtworkNew(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class ArtworkFilter(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'artist',
                        'primary_pallet', 'secondary_pallet', 'medium']


class ArtworkSearch(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class ArtworkDetail(generics.RetrieveAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer


class ArtworkEdit(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
