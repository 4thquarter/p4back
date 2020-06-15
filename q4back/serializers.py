from rest_framework import serializers
from .models import Artist, Artwork, ArtistMedia, ArtworkMedia
from django.contrib.auth.models import User


# class PreArtworkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Artwork
#         fields = '__all__'


class PreArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class ArtistMediaSerializer(serializers.ModelSerializer):
    artist_id = serializers.PrimaryKeyRelatedField(
        read_only=True,
        source='artist'
    )

    class Meta:
        model = ArtistMedia
        fields = '__all__'


class ArtworkMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtworkMedia
        fields = '__all__'

        
class ArtworkSerializer(serializers.ModelSerializer):
    media = ArtworkMediaSerializer(many=True, read_only=True)
    artwork_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artwork_detail'
    )
    class Meta:
        model = Artwork
        fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
    artwork = ArtworkSerializer(many=True, read_only=True)
    media = ArtistMediaSerializer(many=True, read_only=True)
    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail'
    )
    class Meta:
        model = Artist
        fields = '__all__'
