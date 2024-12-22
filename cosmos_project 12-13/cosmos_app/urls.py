from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galaxy/<int:pk>/', views.galaxy_detail, name='galaxy_detail'),
    path('add-galaxy/', views.add_galaxy, name='add_galaxy'),
     path('add-star/', views.add_star, name='add_star'),  # Новый маршрут для добавления звезд
    path('add-planet/', views.add_planet, name='add_planet'),  # Новый маршрут для добавления планет
]
