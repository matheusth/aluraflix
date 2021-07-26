from rest_framework import routers
from django.urls import path, include

from playlist.views import VideosViewSet, CategoriasViewSet

router = routers.DefaultRouter()

router.register('videos', VideosViewSet, basename='videos')
router.register('categorias', CategoriasViewSet, basename='categorias')

urlpatterns = [
    path('', include(router.urls))
]
