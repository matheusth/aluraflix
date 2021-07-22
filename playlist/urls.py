from rest_framework import routers
from django.urls import path, include

from playlist.views import VideoViewSet

router = routers.DefaultRouter()

router.register('videos', VideoViewSet, basename='videos')

urlpatterns = [
    path('', include(router.urls))
]
