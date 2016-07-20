from django.core.management.base import BaseCommand, CommandError
from song.models import Song, Artist, Album, AlbumArtist, Genre, Year
import os.path
import plistlib
from xml.parsers.expat import ExpatError


class Command(BaseCommand):
    help = 'Update song database. By default, the song which already exists will be ignored.'

    def add_arguments(self, parser):
        parser.add_argument('path', help='Path to \'iTunes Music Library.xml\'')
        parser.add_argument('--init', action='store_true', help='Rebuild database')

    def handle(self, *args, **options):
        _entry_point(**options)


def _entry_point(path, **options):
    if not os.path.exists(path):
        raise CommandError('Cannot access \'{}\''.format(path))
    try:
        with open(path, 'rb') as f:
            tracks = _load_tracks(f)
        _song_update(tracks, **options)
    except (FileNotFoundError, PermissionError) as e:
        raise CommandError(e)


def _load_tracks(f):
    try:
        plist = plistlib.load(f)
    except (plistlib.InvalidFileException, ExpatError) as e:
        raise CommandError(e)
    try:
        return plist['Tracks']
    except KeyError as e:
        raise CommandError(e)


def _foreign_field(class_, **value):
    try:
        return class_.objects.get(**value)
    except class_.DoesNotExist:
        n = class_(**value)
        n.save()
        return n


def _register_song(v):
    try:
        song = Song()
        song.persistent_id = v['Persistent ID']
        song.title = v['Name']
        song.track_number = v.get('Track Number', 0)

        song.artist = _foreign_field(Artist, value=v['Artist'])
        song.album = _foreign_field(Album, value=v['Album'], track_count=v.get('Track Count', 0))
        song.album_artist = _foreign_field(AlbumArtist, value=v.get('Album Artist', song.artist.value))
        song.genre = _foreign_field(Genre, value=v['Genre'])
        song.year = _foreign_field(Year, value=v.get('Year', 0))
        song.save()
    except KeyError as e:
        raise CommandError(e)


def _song_update(tracks, **options):
    if options['init']:
        for class_ in (Song, Artist, Album, AlbumArtist, Genre, Year):
            class_.objects.all().delete()

    for v in tracks.values():
        try:
            persistent_id = v['Persistent ID']
        except KeyError as e:
            raise CommandError(e)

        try:
            Song.objects.get(persistent_id=persistent_id)
        except Song.DoesNotExist:
            _register_song(v)
