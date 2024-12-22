from django.contrib import admin
from .models import Galaxy, Star, Planet

@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin):
    list_display = ('name', 'distance_from_earth')
    search_fields = ('name',)

@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ('name', 'galaxy', 'mass')
    list_filter = ('galaxy',)

@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'star', 'has_life')
    list_filter = ('has_life',)
