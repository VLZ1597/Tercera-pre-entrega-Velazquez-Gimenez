from django import forms

class CrearGuitarFormulario(forms.Form):
    marca = forms.CharField(max_length=20)
    forma = forms.CharField(max_length=20)
    