from django.urls import path
from .views import *

urlpatterns = [
    path('actores/', actores, name="actores"),
    path('peliculas/', peliculas, name="peliculas"),
    path('series/', series, name="series"),
    path('busquedaTemporadas/', busquedaTemporadas, name="busquedaTemporadas"),
    path('buscar/', buscar, name="buscar"),
]