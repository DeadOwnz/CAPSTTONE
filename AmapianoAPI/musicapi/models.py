# In musicapi/models.py

from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.artist_name

    class Meta:
        app_label = 'musicapi'

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
