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

def tema_create(request):
    if request.method == 'POST':
        form = forms.TemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clase:home')
    else: #request.method == 'GET':
        form = forms.TemaForm()
    return render(request, 'Clase/tema_create.html', context={'form': form})

def solucion_create(request):
    if request.method == 'POST':
        form = forms.SolucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clase:home')
    else: #request.method == 'GET':
        form = forms.SolucionForm()
    return render(request, 'Clase/solucion_create.html', context={'form': form})