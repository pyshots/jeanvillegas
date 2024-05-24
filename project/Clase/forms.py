from django import forms
from . import models

    #enunciado = models.TextField(blank=True, null=True)
    #tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='ejercicios')
    
    #enunciado = forms.CharField()
    #tema = forms.CharField()

class EjercicioCategoriaForm(forms.ModelForm):
    class Meta:
        model = models.EjercicioCategoria
        fields = ['enunciado', 'tema', 'imagen']  # Solo los campos que se mostrarán en el formulario
        widgets = {
            "enunciado": forms.Textarea(attrs={"class": "form-control", "placeholder": "Enunciado"}),
            "tema": forms.Select(attrs={"class": "form-control"}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control-file"})  # Para la carga de imágenes
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['enunciado'].label = "Enunciado"  # Cambiar la etiqueta del campo enunciado
        self.fields['tema'].label = "Tema"  # Cambiar la etiqueta del campo tema
        self.fields['imagen'].label = "Imagen"

"""class TemaForm(forms.ModelForm):
    class Meta:
        model = models.Tema
        fields = "__all__"
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre"}),
            "curso": forms.Select(attrs={"class": "form-control"}),
        }"""

class SolucionForm(forms.ModelForm):
    class Meta:
        model = models.Solucion
        fields = ['solucion', 'ejercicio_id', 'imagen']  # Asegúrate de incluir el campo 'ejercicio_id'
        widgets = {
            "solucion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Solución"}),
            "ejercicio_id": forms.Select(attrs={"class": "form-control"}),  # Asegúrate de incluir un campo para seleccionar el ejercicio
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control-file"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['solucion'].label = "Solución"
        self.fields['ejercicio_id'].label = "Ejercicio"  # Cambia la etiqueta del campo a "Ejercicio"
        self.fields['imagen'].label = "Imagen"
