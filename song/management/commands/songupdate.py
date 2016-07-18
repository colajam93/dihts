from django.core.management.base import BaseCommand, CommandError
from song.models import Song
import os.path
import plistlib
from xml.parsers.expat import ExpatError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', help='Path to \'iTunes Music Library.xml\'')
        parser.add_argument('-f', '--force', action='store_true', help='Force update')

    def handle(self, *args, **options):
        _entry_point(options['path'], options['force'])


def _entry_point(path, force):
    if not os.path.exists(path):
        raise CommandError('Cannot access \'{}\''.format(path))
    try:
        with open(path, 'rb') as f:
            tracks = _load_tracks(f)
        _song_update(tracks, force)
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


def _song_update(tracks, force):
    for k, v in tracks.items():
        track_id = int(k)
        try:
            song = Song.objects.get(track_id=track_id)
        except Song.DoesNotExist:
            song = Song()
        else:
            if not force:
                continue

        try:
            song.track_id = track_id
            song.title = v['Name']
            song.artist = v['Artist']
            song.album = v['Album']
            song.genre = v['Genre']
            song.year = v.get('Year', 0)
            song.album_artist = v.get('Album Artist', song.artist)
            song.track_number = v.get('Track Number', 0)
            song.track_count = v.get('Track Count', 0)
        except KeyError as e:
            raise CommandError(e)
        song.save()
