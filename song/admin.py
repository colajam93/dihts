from django.contrib import admin
from song.models import Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('persistent_id', 'title', 'artist', 'album')


admin.site.register(Song, SongAdmin)
