from django.urls import path
from . import views
app_name = 'Clase'

urlpatterns = [
    path("", views.home, name="home"),
    path("ejerciciocategoria/create/", views.ejerciciocategoria_create, name="ejerciciocategoria_create"),
    path("tema/create/", views.tema_create, name="tema_create"),
    path("solucion/create/", views.solucion_create, name="solucion_create"),
]
