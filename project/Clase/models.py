from django.db import models
from datetime import datetime

class Ciclo(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=100, unique=True, blank=True, null=True)
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name='cursos')
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, related_name='cursos')
    
    def __str__(self):
        return self.nombre

class Tema(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='temas')
    
    def __str__(self):
        return self.nombre

class EjercicioCategoria(models.Model):
    enunciado = models.TextField(blank=True, null=True)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='ejercicios')
    fecha_creacion = models.DateField(default=datetime.now, blank=True, null=True, editable=False)
    imagen = models.ImageField(upload_to='ejercicios/', blank=True, null=True)
    
    def __str__(self):
        return f"Ejercicio numero {self.id}"

class Solucion(models.Model):
    solucion = models.TextField(blank=True, null=True)
    ejercicio_id = models.ForeignKey(EjercicioCategoria, on_delete=models.CASCADE, related_name='soluciones')
    fecha_creacion = models.DateField(default=datetime.now, blank=True, null=True, editable=False)
    imagen = models.ImageField(upload_to='soluciones/', blank=True, null=True)
    
    def __str__(self):
        return f"Solución del ejercicio número {self.ejercicio_id.id}"
