from django.http import HttpResponse
from song.models import Song
import json


def _load_filter_condition(condition_json):
    c = json.loads(condition_json)
    return {c['target']: c['value']}


def search(request):
    conditions = request.GET.getlist('condition[]')
    songs = Song.objects.all()
    for condition in conditions:
        try:
            filer_condition = _load_filter_condition(condition)
        except (json.JSONDecodeError, KeyError):
            continue
        else:
            songs = songs.filter(**filer_condition)

    return HttpResponse('<br>'.join(map(lambda x: str(x), songs)))
