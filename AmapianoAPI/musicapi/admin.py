from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Artist, Genre, Platform

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Platform)
