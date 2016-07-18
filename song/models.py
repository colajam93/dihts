from django.db import models

_MAX_LENGTH = 100


class Song(models.Model):
    title = models.CharField(max_length=_MAX_LENGTH)
    artist = models.CharField(max_length=_MAX_LENGTH)
    album = models.CharField(max_length=_MAX_LENGTH)
    album_artist = models.CharField(max_length=_MAX_LENGTH)
    genre = models.CharField(max_length=_MAX_LENGTH)
    track_number = models.IntegerField()
    track_count = models.IntegerField()
    year = models.IntegerField()
