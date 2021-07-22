from rest_framework import serializers
from playlist.models import Video


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
