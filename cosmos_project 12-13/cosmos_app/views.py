from django.shortcuts import render, redirect, get_object_or_404
from .models import Galaxy
from .forms import GalaxyForm
from .forms import StarForm
from .forms import PlanetForm

# Главная страница
def home(request):
    galaxies = Galaxy.objects.all()
    return render(request, 'cosmos_app/home.html', {'galaxies': galaxies})

# Детальная информация о галактике
def galaxy_detail(request, pk):
    galaxy = get_object_or_404(Galaxy, pk=pk)
    return render(request, 'cosmos_app/galaxy_detail.html', {'galaxy': galaxy})

# Добавление галактики
def add_galaxy(request):
    if request.method == "POST":
        form = GalaxyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Возврат на главную страницу после добавления
    else:
        form = GalaxyForm()
    return render(request, 'cosmos_app/add_galaxy.html', {'form': form})

def add_star(request):
    if request.method == "POST":
        form = StarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # После добавления вернёт на главную
    else:
        form = StarForm()
    return render(request, 'cosmos_app/add_star.html', {'form': form})

# Добавление планеты
def add_planet(request):
    if request.method == "POST":
        form = PlanetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # После добавления вернёт на главную
    else:
        form = PlanetForm()
    return render(request, 'cosmos_app/add_planet.html', {'form': form})