from rest_framework import serializers
from .models import Artist, Artwork, ArtistImage, ArtworkImage


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    artwork = serializers.HyperlinkedRelatedField(
        view_name='',
        #not using templates?
        many=True,
        read_only=True
    )
    artist_url = serializers.ModelSerializer.serializer_url_field(
        view_name=''
        #same issue
    )

    class Meta:
    model = Artist
    fields = (
        'id', 'email', 'information',
    )


class ArtistworkSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.HyperlinkedRelatedField(
        view_name='',
        #template issue
        read_only=True
    )
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )

    class Meta:
        model = Artwork
        fields = ('id', 'artist', 'artist_id', 'title', 'description',)


# Not sure if I need to add ArtistImage and ArtistWork.
# If so then it would just reflect what model its connected to and just use a url for the fields, since its just images.
