from django.db import models

_MAX_LENGTH = 100


class AlbumArtist(models.Model):
    value = models.CharField(max_length=_MAX_LENGTH)

    def __str__(self):
        return self.value


class Genre(models.Model):
    value = models.CharField(max_length=_MAX_LENGTH)

    def __str__(self):
        return self.value


class Year(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)


class Artist(models.Model):
    artist = models.CharField(max_length=_MAX_LENGTH)
    genre = models.ForeignKey(Genre)

    def __str__(self):
        return self.artist


class Album(models.Model):
    album = models.CharField(max_length=_MAX_LENGTH)
    track_count = models.IntegerField(blank=True)
    album_artist = models.ForeignKey(AlbumArtist)
    year = models.ForeignKey(Year)

    def __str__(self):
        return self.album


class Song(models.Model):
    persistent_id = models.CharField(max_length=_MAX_LENGTH)
    title = models.CharField(max_length=_MAX_LENGTH)
    track_number = models.IntegerField()

    # ForeignKey fields
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)

    def __str__(self):
        return '{} - {} - {}'.format(self.title, self.artist, self.album)
