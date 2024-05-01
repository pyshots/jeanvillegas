from django.shortcuts import render, redirect

from . import models, forms

def home(request):
    query = models.Ciclo.objects.all().prefetch_related('cursos__profesor', 'cursos__temas__ejercicios__solucion')
    context = {'ciclos': query}
    return render(request, 'Clase/index.html', context)

def ejerciciocategoria_create(request):
    if request.method == 'POST':
        form = forms.EjercicioCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clase:home')
    else: #request.method == 'GET':
        form = forms.EjercicioCategoriaForm()
    return render(request, 'Clase/ejerciciocategoria_create.html', context={'form': form})