from django import forms
from django.forms import ModelForm

from .models import Publicacion

class PublicacionForm(ModelForm):
    class Meta:
        model = Publicacion
        fields = ('titulo', 'descripcion', 'imagen')
        labels ={
            'titulo':'Titulo',
            'descripcion':'Descripcion',
        }
        widgets = {
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'descripcion':forms.Textarea(attrs={'class':'form-control'}),
        }

