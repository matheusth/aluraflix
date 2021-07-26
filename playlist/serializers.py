from rest_framework import serializers
from playlist.models import Video, Categoria


class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
