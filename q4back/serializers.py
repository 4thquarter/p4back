from rest_framework import serializers
from .models import Artist, Artwork, ArtistMedia, ArtworkMedia
from django.contrib.auth.models import User


class PreArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = '__all__'

class PreArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artist
        fields='__all__'

class ArtistSerializer(serializers.ModelSerializer):
    artwork = PreArtworkSerializer(many=True, read_only=True)
    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail'
    )

    class Meta:
        model = Artist
        fields = '__all__'


class ArtworkSerializer(serializers.ModelSerializer):
    artist = PreArtistSerializer(read_only=True)
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = Artwork
        fields = '__all__'




class ArtworkMediaSerializer(serializers.ModelSerializer):
    artwork_id = serializers.PrimaryKeyRelatedField(
        queryset=Artwork.objects.all(),
        source='artwork'
    )

    class Meta:
        model = ArtworkMedia
        fields = '__all__' 


class ArtistMediaSerializer(serializers.ModelSerializer):
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = ArtworkMedia
        fields = '__all__'
