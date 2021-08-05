from rest_framework import viewsets, generics
from playlist.models import Video, Categoria
from playlist.serializers import VideosSerializer, CategoriasSerializer, VideosByCategoria


class VideosViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideosSerializer


class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriasSerializer


class VideosCategoriaViewSet(generics.ListAPIView):
    def get_queryset(self):
        videos = Video.objects.filter(categoria_id=self.kwargs['pk'])
        return videos

    serializer_class = VideosByCategoria
