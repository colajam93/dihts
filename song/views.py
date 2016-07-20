from django.shortcuts import render
from song.models import Song, Album
from django.views.decorators.csrf import ensure_csrf_cookie

SEARCH_FOR, SEARCH_TYPE, KEYWORD, RESULTS = ('search_for', 'search_type', 'keyword', 'results')
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
        keyword = request.GET[KEYWORD]
        params[KEYWORD] = keyword
        if search_for == ALBUM:
            filter_param = {'value__{}'.format(search_type): keyword}
            params[RESULTS] = map(lambda x: {'column1': x.value},
                                  Album.objects.filter(**filter_param).order_by('value'))
        elif search_for == SONG:
            filter_param = {'title__{}'.format(search_type): keyword}
            params[RESULTS] = map(lambda x: {'column1': x.title, 'column2': x.artist, 'column3': x.album},
                                  Song.objects.filter(**filter_param).order_by('album__value', 'artist__value',
                                                                               'title'))
    except KeyError:
        params[RESULTS] = []
        params[KEYWORD] = ''

    return render(request, 'search.html', params)
