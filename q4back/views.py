from rest_framework import generics, permissions
from .serializers import ArtistSerializer, ArtworkSerializer, ArtworkMediaSerializer
from .models import Artist, Artwork, ArtistMedia, ArtworkMedia
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from q4back.permissions import IsOwnerOrReadOnly


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name', 'email']
    search_fields = ['name', 'email', 'information']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ArtworkList(generics.ListCreateAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'artist',
                        'primary_palette', 'secondary_palette', 'medium']
    search_fields = ['title', 'description']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArtworkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ArtworkMediaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtworkMedia.objects.all()
    serializer_class = ArtworkMediaSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ArtworkMediaList(generics.ListCreateAPIView):
    queryset = ArtworkMedia.objects.all()
    serializer_class = ArtworkMediaSerializer
