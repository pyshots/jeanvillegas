from django.shortcuts import render

from . import models

def home(request):
    query = models.Ciclo.objects.all().prefetch_related('cursos__profesor', 'cursos__temas__ejercicios__solucion')
    context = {'ciclos': query}
    return render(request, 'Clase/index.html', context)