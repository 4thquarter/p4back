# Generated by Django 3.0.7 on 2020-06-09 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('information', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('primary_pallet', models.CharField(max_length=100)),
                ('secondary_pallet', models.CharField(max_length=100)),
                ('medium', models.CharField(max_length=100)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artwork', to='q4back.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='ArtworkImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField()),
                ('artwork_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artwork_image', to='q4back.Artwork')),
            ],
        ),
        migrations.CreateModel(
            name='ArtistImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.TextField()),
                ('artist_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist_image', to='q4back.Artist')),
            ],
        ),
    ]