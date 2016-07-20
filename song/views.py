from django.shortcuts import render
from song.models import Song
from django.views.decorators.csrf import ensure_csrf_cookie

SEARCH_FOR, SEARCH_TYPE, SONGS, = ('search_for', 'search_type', 'songs')
ALBUM, SONG = ('album', 'song')
CONTAINS, EXACT, STARTSWITH, ENDSWITH = ('contains', 'exact', 'startswith', 'endswith')


@ensure_csrf_cookie
def search(request):
    params = {}
    search_for = request.GET.get(SEARCH_FOR, ALBUM)
    params[SEARCH_FOR] = search_for
    search_type = request.GET.get(SEARCH_TYPE, CONTAINS)
    params[SEARCH_TYPE] = search_type

    try:
        keyword = request.GET['keyword']
        params[SONGS] = Song.objects.filter(title__contains=keyword)
    except KeyError:
        params[SONGS] = []

    return render(request, 'search.html', params)
