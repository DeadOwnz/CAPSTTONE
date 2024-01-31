# musicapi/views.py
from django.http import HttpResponse
from rest_framework import generics
from .models import Artist, Genre, Platform
from .serializers import ArtistSerializer, GenreSerializer, PlatformSerializer

class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class PlatformList(generics.ListCreateAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer

def home(request):
    return HttpResponse("Welcome to the AmapianoAPI!")
