from django.contrib import admin
from song.models import Song, Artist, Album, AlbumArtist, Genre, Year


class SongAdmin(admin.ModelAdmin):
    list_display = ('persistent_id', 'title', 'artist', 'album', 'album_artist', 'genre', 'year', 'track_number')


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('value',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('value', 'track_count')


class AlbumArtistAdmin(admin.ModelAdmin):
    list_display = ('value',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('value',)


class YearAdmin(admin.ModelAdmin):
    list_display = ('value',)


admin.site.register(Song, SongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumArtist, AlbumArtistAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Year, YearAdmin)
