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