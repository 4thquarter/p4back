from django.db import models
from time import time
from django.conf import settings
from users.models import User


# Create your models here.


def upload_media(instance, filename):
    ext = filename.split('.')[-1]
    newfilename = f'{instance.name}{round(time())}.{ext}'
    return f'artwork/{newfilename}'


class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    information = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    artist_website = models.TextField(blank=True, null=True)
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
    MEDIUM_CHOICES = (
        ('none', 'none'),
        ('sculpture', 'sculpture'),
        ('flat art', 'flat art'),
        ('audio', 'audio'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    primary_palette = models.CharField(
        max_length=6, choices=PALETTE_CHOICES, default='none',)
    secondary_palette = models.CharField(
        max_length=6, choices=PALETTE_CHOICES, default='none',)
    medium = models.CharField(
        max_length=9, choices=MEDIUM_CHOICES, default='none')
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='artwork')
    owner = models.ForeignKey(
        User, related_name='artworks', on_delete=models.CASCADE)


class ArtistMedia(models.Model):
    name = models.CharField(max_length=100)
    media_url = models.ImageField(upload_to=upload_media)
    owner = models.ForeignKey(
        User, related_name='artistmedias', on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class ArtworkMedia(models.Model):
    name = models.CharField(max_length=100)
    media_url = models.ImageField(
        upload_to=upload_media)
    owner = models.ForeignKey(
        User, related_name='artworkmedias', on_delete=models.CASCADE)
    artwork = models.ForeignKey(
        Artwork, related_name='media', on_delete=models.CASCADE)
