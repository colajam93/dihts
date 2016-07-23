from django.contrib import admin
from song.models import Song, Artist, Album, AlbumArtist, Genre


class SongAdmin(admin.ModelAdmin):
    list_display = ('persistent_id', 'title', 'artist', 'album', 'track_number')


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('artist',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album', 'track_count', 'album_artist')


class AlbumArtistAdmin(admin.ModelAdmin):
    list_display = ('value', 'genre')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('value',)


admin.site.register(Song, SongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(AlbumArtist, AlbumArtistAdmin)
admin.site.register(Genre, GenreAdmin)
