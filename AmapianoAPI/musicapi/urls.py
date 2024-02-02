# musicapi/urls.py
# musicapi/urls.py
from django.urls import path, include
from .views import ArtistList, GenreList, PlatformList, home
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="AmapianoAPI",
        default_version='v1',
        description="Amapiano X Connection",
        terms_of_service="https://yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('artists/', ArtistList.as_view(), name='artist-list'),
    path('genres/', GenreList.as_view(), name='genre-list'),
    path('platforms/', PlatformList.as_view(), name='platform-list'),
    path('', home, name='home'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
