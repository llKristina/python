from django import forms
from .models import Galaxy, Star, Planet

# Существующая форма для галактики
class GalaxyForm(forms.ModelForm):
    class Meta:
        model = Galaxy
        fields = ['name', 'description', 'distance_from_earth']

# Новая форма для звезд
class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = ['name', 'galaxy', 'mass', 'brightness']

# Новая форма для планет
class PlanetForm(forms.ModelForm):
    class Meta:
        model = Planet
        fields = ['name', 'star', 'has_life']
