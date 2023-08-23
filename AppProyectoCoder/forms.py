from django import forms


class ActorForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)

class PeliculaForm(forms.Form):
    titulo=forms.CharField(max_length=50)
    genero=forms.CharField(max_length=50)

class SerieForm(forms.Form):
    titulo=forms.CharField(max_length=50)
    temporadas=forms.IntegerField()