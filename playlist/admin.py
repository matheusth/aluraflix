from django.contrib import admin

from playlist.models import Video


@admin.register(Video)
class Video(admin.ModelAdmin):
    list_display = ['id','titulo', 'descricao']
    list_display_links = ['id', 'titulo']