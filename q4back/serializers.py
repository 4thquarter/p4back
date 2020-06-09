from rest_framework import serializers
from .models import Artist, Artwork, ArtistImage, ArtworkImage


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    artwork = serializers.HyperlinkedRelatedField(
        view_name='artwork_detail',
        many=True,
        read_only=True
    )
    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name='artist_detail'
        
    )

    class Meta:
        model = Artist
        fields = (
            'id', 'email', 'information', 'artist_url', 'artwork',
    )


class ArtworkSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='artist_detail',
        read_only=True
    )
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = Artwork
        fields = ('id', 'artist', 'artist_id', 'title', 'description',)
