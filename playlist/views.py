from rest_framework import viewsets
from playlist.models import Video
from playlist.serializers import VideosSerializer


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideosSerializer
