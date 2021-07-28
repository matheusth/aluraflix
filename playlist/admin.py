from django.contrib import admin

from playlist.models import Video, Categoria


@admin.register(Video)
class Videos(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'descricao']
    list_display_links = ['id', 'titulo']


@admin.register(Categoria)
class Categorias(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'cor']
    list_display_links = ['id', 'titulo']
