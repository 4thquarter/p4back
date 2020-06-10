from django.db import models
from time import time

# Create your models here.


def upload_image(instance, filename):
    ext = filename.split('.')[-1]
    newfilename = f'{instance.name}{round(time())}.{ext}'
    return f'artwork/{newfilename}'


class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    information = models.TextField()


class Artwork(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='artwork')
    primary_pallet = models.CharField(max_length=100)
    secondary_pallet = models.CharField(max_length=100)
    medium = models.CharField(max_length=100)


class ArtistImage(models.Model):
    artist_image = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='artist_image')
    image_url = models.TextField()


class ArtworkImage(models.Model):
    artwork_image = models.ForeignKey(
        Artwork, on_delete=models.CASCADE, related_name='artwork_image')
    image_url = models.ImageField(upload_to=upload_image, blank=True)
