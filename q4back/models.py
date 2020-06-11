from django.db import models
from time import time
from django.conf import settings
from users.models import User

# Create your models here.


def upload_media(instance, filename):
    ext = filename.split('.')[-1]
    newfilename = f'{instance.name}{round(time())}.{ext}'
    return f'artwork/{newfilename}'


class ArtistMedia(models.Model):
    media_url = models.ImageField(upload_to=upload_media, blank=True)
    owner = models.ForeignKey(
        User, related_name='artistmedias', on_delete=models.CASCADE)


class ArtworkMedia(models.Model):
    media_url = models.ImageField(upload_to=upload_media, blank=True)
    owner = models.ForeignKey(
        User, related_name='artworkmedias', on_delete=models.CASCADE)



class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    information = models.TextField()
    location = models.CharField(max_length=100)
    artist_website = models.TextField()
    artist_media = models.ForeignKey(
        ArtistMedia, on_delete=models.CASCADE, related_name='artist_media')
    owner = models.ForeignKey(
        User, related_name='artists', on_delete=models.CASCADE)


class Artwork(models.Model):
    PALETTE_CHOICES = (
        ('none', 'none'),
        ('light', 'light'),
        ('dark', 'dark'),
        ('blue', 'blue'),
        ('yellow', 'yellow'),
        ('red', 'red'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    primary_palette = models.CharField(
        max_length=6, choices=PALETTE_CHOICES, default='none',)
    secondary_palette = models.CharField(
        max_length=6, choices=PALETTE_CHOICES, default='none',)
    medium = models.CharField(max_length=100)
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='artwork')
    artwork_media = models.ForeignKey(
        ArtworkMedia, on_delete=models.CASCADE, related_name='artwork_media')
    owner = models.ForeignKey(
        User, related_name='artworks', on_delete=models.CASCADE)
