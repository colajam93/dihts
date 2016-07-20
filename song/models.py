from django.db import models

_MAX_LENGTH = 100


class Artist(models.Model):
    value = models.CharField(max_length=_MAX_LENGTH)

    def __str__(self):
        return self.value


class Album(models.Model):
    value = models.CharField(max_length=_MAX_LENGTH)
    track_count = models.IntegerField(blank=True)

    def __str__(self):
        return self.value


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


class Song(models.Model):
    persistent_id = models.CharField(max_length=_MAX_LENGTH)
    title = models.CharField(max_length=_MAX_LENGTH)
    track_number = models.IntegerField()

    # ForeignKey fields
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)
    album_artist = models.ForeignKey(AlbumArtist)
    genre = models.ForeignKey(Genre)
    year = models.ForeignKey(Year)

    def __str__(self):
        return '{} - {} - {}'.format(self.title, self.artist, self.album)
