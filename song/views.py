from django.shortcuts import render
from song.models import Song, Album
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.paginator import Paginator

FOR, IN, KEYWORD, MATCH, RESULTS = ('for', 'in', 'keyword', 'match', 'results')
ALBUM, SONG = ('album', 'song')
TITLE, ARTIST, GENRE, ALBUM_ARTIST, YEAR = ('title', 'artist', 'genre', 'album_artist', 'year')
CONTAINS, EXACT, FORWARD, BACKWARD = ('contains', 'exact', 'forward', 'backward')


def _match_suffix(match):
    if match == CONTAINS:
        return '{}__contains'
    elif match == EXACT:
        return '{}__exact'
    elif match == FORWARD:
        return '{}__startswith'
    elif match == BACKWARD:
        return '{}__endswith'


def _search_album(**params):
    search_in = params[IN]
    match_suffix = _match_suffix(params[MATCH])
    q = ''
    if search_in == TITLE:
        q = 'album'
    elif search_in == ARTIST:
        q = 'album_artist__value'
    elif search_in == GENRE:
        q = 'album_artist__genre__value'
    elif search_in == ALBUM_ARTIST:
        q = 'album_artist__value'
    elif search_in == YEAR:
        q = 'year__value'
    query = {match_suffix.format(q): params[KEYWORD]}
    result = Album.objects.filter(**query).order_by('album', 'album_artist')
    return list(map(lambda x: {'title': x.album, 'album_artist': x.album_artist, 'artist': '', 'album': ''}, result))


def _search_song(**params):
    search_in = params[IN]
    match_suffix = _match_suffix(params[MATCH])
    q = ''
    if search_in == TITLE:
        q = 'title'
    elif search_in == ARTIST:
        q = 'artist__artist'
    elif search_in == GENRE:
        q = 'album__album_artist__genre__value'
    elif search_in == ALBUM_ARTIST:
        q = 'album__album_artist__value'
    elif search_in == YEAR:
        q = 'album__year__value'
    query = {match_suffix.format(q): params[KEYWORD]}
    result = Song.objects.filter(**query).order_by('album__album_artist', 'album', 'title', 'artist')
    return list(
        map(lambda x: {'title': x.title, 'album_artist': x.album.album_artist, 'artist': x.artist, 'album': x.album},
            result))


@ensure_csrf_cookie
def search(request):
    search_for = request.GET.get(FOR, ALBUM)
    search_in = request.GET.get(IN, TITLE)
    search_keyword = request.GET.get(KEYWORD, '')
    search_match = request.GET.get(MATCH, CONTAINS)
    params = {FOR: search_for, IN: search_in, KEYWORD: search_keyword, MATCH: search_match}

    result = []
    if search_keyword:
        if search_for == ALBUM:
            result = _search_album(**params)
        elif search_for == SONG:
            result = _search_song(**params)
    page = int(request.GET.get('page', 1))
    params[RESULTS] = Paginator(result, 20).page(page)

    return render(request, 'search.html', params)
