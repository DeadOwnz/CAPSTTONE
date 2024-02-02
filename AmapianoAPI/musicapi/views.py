# musicapi/views.py
from django.shortcuts import render
from .models import Artist, Genre, Platform
from .serializers import ArtistSerializer, GenreSerializer, PlatformSerializer
from django.http import HttpResponse
from rest_framework import generics

class ArtistList(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class GenreList(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlatformList(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

def home(request):
    artists = Artist.objects.all()
    genres = Genre.objects.all()
    platforms = Platform.objects.all()

    return render(
        request,
        'home.html',
        {'artists': artists, 'genres': genres, 'platforms': platforms}
    )
