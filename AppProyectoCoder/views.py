from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def inicio(request):
   return render(request, "AppProyectoCoder/inicio.html")

def actores(request):
   if request.method=="POST":
      form=ActorForm(request.POST)
      if form.is_valid():
         info=form.cleaned_data
         nombre=info["nombre"]
         apellido=info["apellido"]
         actor=Actor(nombre=nombre,apellido=apellido)
         actor.save()
         formulario_actor=ActorForm()
         return render(request,"AppProyectoCoder/actores.html",{"mensaje":"ACTOR CREADO","formulario":formulario_actor})
      else:
         return render(request,"AppProyectoCoder/actores.html",{"mensaje":"DATOS INVALIDOS","formulario":formulario_actor})
   else:
      formulario_actor=ActorForm()
      return render(request, "AppProyectoCoder/actores.html", {"formulario":formulario_actor})
   
def peliculas(request):
   if request.method=="POST":
      form=PeliculaForm(request.POST)
      if form.is_valid():
         info=form.cleaned_data
         titulo=info["titulo"]
         genero=info["genero"]
         pelicula=Pelicula(titulo=titulo,genero=genero)
         pelicula.save()
         formulario_pelicula=PeliculaForm()
         return render(request,"AppProyectoCoder/peliculas.html",{"mensaje":"PELICULA CREADA","formulario":formulario_pelicula})
      else:
         return render(request,"AppProyectoCoder/peliculas.html",{"mensaje":"DATOS INVALIDOS","formulario":formulario_pelicula})
   else:
      formulario_pelicula=PeliculaForm()
      return render(request, "AppProyectoCoder/peliculas.html", {"formulario":formulario_pelicula})
   
def series(request):
   if request.method=="POST":
      form=SerieForm(request.POST)
      if form.is_valid():
         info=form.cleaned_data
         titulo=info["titulo"]
         temporadas=info["temporadas"]
         serie=Serie(titulo=titulo,temporadas=temporadas)
         serie.save()
         formulario_serie=SerieForm()
         return render(request,"AppProyectoCoder/series.html",{"mensaje":"SERIE CREADA","formulario":formulario_serie})
      else:
         return render(request,"AppProyectoCoder/series.html",{"mensaje":"DATOS INVALIDOS","formulario":formulario_serie})
   else:
      formulario_serie=SerieForm()
      return render(request, "AppProyectoCoder/series.html", {"formulario":formulario_serie})
   
def busquedaTemporadas(request):
   return render(request, "AppProyectoCoder/busquedaTemporadas.html")

def buscar(request):
   temporadas=request.GET["temporadas"]
   if temporadas!="":
      series=Serie.objects.filter(temporadas=temporadas)
      return render(request, "AppProyectoCoder/resultadosBusqueda.html", {"series":series})
   else:
      return render(request, "AppProyectoCoder/resultadosBusqueda.html", {"mensaje":"NO HA INGRESADO CANTIDAD DE TEMPORADAS"})
   