from rest_framework import serializers
from playlist.models import Video, Categoria


class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class VideosSerializer(serializers.ModelSerializer):
    categoria = CategoriasSerializer(many=False, allow_null=True, read_only=True)
    categoria_cor = serializers

    class Meta:
        model = Video
        fields = '__all__'


class VideosByCategoria(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
