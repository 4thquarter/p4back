from rest_framework import generics
from .serializers import ArtistSerializer, ArtistWorkSerializer
from .models import Artist, Artwork, ArtistImage, ArtworkImage


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.object.all()
    serializer_class = ArtistSerializer

    # started on views
