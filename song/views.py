from django.shortcuts import render
from song.models import Song
import json
from django.views.decorators.csrf import ensure_csrf_cookie


def _load_filter_condition(condition_json):
    c = json.loads(condition_json)
    return {c['target']: c['value']}


@ensure_csrf_cookie
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

    return render(request, 'search.html', {'songs': songs})
