from rest_framework import serializers
from .models import Artist, Artwork, ArtistImage, ArtworkImage


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
    artist = PreArtistSerializer()
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = Artwork
        fields = '__all__'
