from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.http import HttpRequest, HttpResponse

#@login_required
def home(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'
    next_page = '/'

def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'core/index.html', {'mensaje': "usuario creado"})
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})