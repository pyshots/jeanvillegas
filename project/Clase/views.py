from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'Clase/index.html')

"""def ejerciciocategoria_list(request):
    consulta = request.GET.get("consulta", None)
    if consulta:
        cursos = models.Curso.objects.filter(nombre__icontains=consulta)
    else:
        cursos = models.Curso.objects.all()
    context = {"cursos": cursos}
    return render(request, 'Clase/ejerciciocategoria_list.html', context)"""

class EjercicioCategoriaCreate(LoginRequiredMixin, CreateView):
    model = models.EjercicioCategoria
    form_class = forms.EjercicioCategoriaForm
    success_url = reverse_lazy('Clase:home')

class EjercicioCategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = models.EjercicioCategoria
    form_class = forms.EjercicioCategoriaForm
    success_url = reverse_lazy('Clase:ejerciciocategoria_list')

class EjercicioCategoriaDelete(LoginRequiredMixin, DeleteView):
    model = models.EjercicioCategoria
    success_url = reverse_lazy('Clase:ejerciciocategoria_list')

"""class EjercicioCategoriaList(ListView):
    model = models.EjercicioCategoria
    context_object_name = 'ejercicios'
    template_name = 'Clase/ejerciciocategoria_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = models.Curso.objects.all()
        return context

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.EjercicioCategoria.objects.filter(enunciado__icontains=consulta)
        else:
            object_list = models.EjercicioCategoria.objects.all()
        return object_list"""

class EjercicioCategoriaList(LoginRequiredMixin, ListView):
    model = models.Curso
    context_object_name = 'cursos'
    template_name = 'Clase/ejerciciocategoria_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.GET.get("consulta")
        if consulta:
            queryset = queryset.filter(nombre__icontains=consulta)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consulta'] = self.request.GET.get("consulta", "")
        return context

class EjercicioCategoriaDetail(LoginRequiredMixin, DetailView):
    model = models.EjercicioCategoria
    context_object_name = 'ejercicio'
    template_name = 'Clase/ejerciciocategoria_detail.html'

"""def ejerciciocategoria_create(request):
    if request.method == 'POST':
        form = forms.EjercicioCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clase:home')
    else:  # request.method == 'GET':
        form = forms.EjercicioCategoriaForm()
    return render(request, 'Clase/ejerciciocategoria_create.html', context={'form': form})"""

def tema_create(request):
    if request.method == 'POST':
        form = forms.TemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clase:home')
    else:  # request.method == 'GET':
        form = forms.TemaForm()
    return render(request, 'Clase/tema_create.html', context={'form': form})

def solucion_create(request):
    if request.method == 'POST':
        form = forms.SolucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Clase:home')
    else:  # request.method == 'GET':
        form = forms.SolucionForm()
    return render(request, 'Clase/solucion_create.html', context={'form': form})
