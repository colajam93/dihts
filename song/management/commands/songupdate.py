from django.core.management.base import BaseCommand, CommandError
from song.models import Song
import os.path
import plistlib
from xml.parsers.expat import ExpatError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', help='Path to \'iTunes Music Library.xml\'')
        parser.add_argument('-f', '--force', action='store_true', help='Force update')
        parser.add_argument('--init', action='store_true', help='Initialize')

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


def _song_update(tracks, **options):
    for v in tracks.values():
        persistent_id = v['Persistent ID']
        song = Song()
        if not options['init']:
            try:
                song = Song.objects.get(persistent_id=persistent_id)
            except Song.DoesNotExist:
                pass
            else:
                if not options['force']:
                    continue

        try:
            song.persistent_id = persistent_id
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
