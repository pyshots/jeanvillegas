from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models, forms

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

class EjercicioCategoriaCreate(CreateView):
    model = models.EjercicioCategoria
    form_class = forms.EjercicioCategoriaForm
    success_url = reverse_lazy('Clase:home')

class EjercicioCategoriaUpdate(UpdateView):
    model = models.EjercicioCategoria
    form_class = forms.EjercicioCategoriaForm
    success_url = reverse_lazy('Clase:ejerciciocategoria_list')

class EjercicioCategoriaDelete(DeleteView):
    model = models.EjercicioCategoria
    success_url = reverse_lazy('Clase:ejerciciocategoria_list')

class EjercicioCategoriaList(ListView):
    model = models.EjercicioCategoria
    context_object_name = 'ejercicios'
    template_name = 'Clase/ejerciciocategoria_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = models.Curso.objects.all()
        return context

class EjercicioCategoriaDetail(DetailView):
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
