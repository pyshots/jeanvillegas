from django.db import models

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
    
    def __str__(self):
        return f"Ejercicio numero {self.id} ({self.tema.nombre})"

class Solucion(models.Model):
    solucion = models.TextField(blank=True, null=True)
    ejercicio = models.OneToOneField(EjercicioCategoria, on_delete=models.CASCADE, related_name='solucion')
    
    def __str__(self):
        return f"Solución del ejercicio número {self.ejercicio.id} ({self.ejercicio.tema.nombre})"
