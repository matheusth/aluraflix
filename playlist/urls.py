from rest_framework import routers
from django.urls import path, include

from playlist.views import VideosViewSet, CategoriasViewSet, VideosCategoriaViewSet

router = routers.DefaultRouter()

router.register(r'videos', VideosViewSet, basename='videos')
router.register(r'categorias', CategoriasViewSet, basename='categorias')

urlpatterns = [
    path('', include(router.urls)),
    path('categorias/<int:pk>/videos',VideosCategoriaViewSet.as_view(), name='videos-categoria')
]
