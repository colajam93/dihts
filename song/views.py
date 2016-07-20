from django.shortcuts import render
from song.models import Song
from django.views.decorators.csrf import ensure_csrf_cookie

SEARCH_FOR, ALBUM, SONGS, SONG = ('search_for', 'album', 'songs', 'song')


@ensure_csrf_cookie
def search(request):
    params = {}
    search_for = request.GET.get(SEARCH_FOR, ALBUM)
    params[SEARCH_FOR] = search_for

    try:
        keyword = request.GET['keyword']
        params[SONGS] = Song.objects.filter(title__contains=keyword)
    except KeyError:
        params[SONGS] = []

    return render(request, 'search.html', params)
