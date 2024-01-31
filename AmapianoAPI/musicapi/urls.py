# musicapi/urls.py
from django.urls import path
from .views import ArtistList, GenreList, PlatformList

urlpatterns = [
    path('artists/', ArtistList.as_view(), name='artist-list'),
    path('genres/', GenreList.as_view(), name='genre-list'),
    path('platforms/', PlatformList.as_view(), name='platform-list'),
]
