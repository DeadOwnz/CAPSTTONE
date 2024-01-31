from django.test import TestCase
from rest_framework.test import APIClient
from .models import Artist, Genre, Platform

class ArtistTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Artist.objects.create(name='Kabza de Small')

    def test_get_artist_list(self):
        response = self.client.get('/artists/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kabza de Small')

class GenreTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Genre.objects.create(name='Amapiano')

    def test_get_genre_list(self):
        response = self.client.get('/genres/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Amapiano')

class PlatformTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        Platform.objects.create(name='Spotify')

    def test_get_platform_list(self):
        response = self.client.get('/platforms/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Spotify')
