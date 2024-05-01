from django import forms
from . import models

    #enunciado = models.TextField(blank=True, null=True)
    #tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='ejercicios')
    
    #enunciado = forms.CharField()
    #tema = forms.CharField()

class EjercicioCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.EjercicioCategoria
        fields = "__all__"
        widgets = {
            "enunciado": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enunciado"}),
            "tema": forms.Select(attrs={"class": "form-control"}),
        }

class TemaForm(forms.ModelForm):
    class Meta:
        model = models.Tema
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "curso": forms.Select(attrs={"class": "form-control"}),
        }

class SolucionForm(forms.ModelForm):
    class Meta:
        model = models.Solucion
        fields = "__all__"
        widgets = {
            "solucion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Solución"}),
            "ejercicio": forms.Select(attrs={"class": "form-control"}),
        }