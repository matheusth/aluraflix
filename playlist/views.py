from rest_framework import viewsets
from playlist.models import Video, Categoria
from playlist.serializers import VideosSerializer, CategoriasSerializer


class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideosSerializer


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriasSerializer
