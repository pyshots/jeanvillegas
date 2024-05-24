from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
app_name = 'Clase'

urlpatterns = [
    path("", views.home, name="home"),
    #path("ejerciciocategoria/create/", views.ejerciciocategoria_create, name="ejerciciocategoria_create"),
    path("ejerciciocategoria/create/", views.EjercicioCategoriaCreate.as_view(), name="ejerciciocategoria_create"),
    #path("ejerciciocategoria/list/", views.ejerciciocategoria_list, name="ejerciciocategoria_list"),
    path("ejerciciocategoria/list/", views.EjercicioCategoriaList.as_view(), name="ejerciciocategoria_list"),
    path("ejerciciocategoria/detail/<int:pk>/", views.EjercicioCategoriaDetail.as_view(), name="ejerciciocategoria_detail"),
    path("ejerciciocategoria/update/<int:pk>/", views.EjercicioCategoriaUpdate.as_view(), name="ejerciciocategoria_update"),
    path("ejerciciocategoria/delete/<int:pk>/", views.EjercicioCategoriaDelete.as_view(), name="ejerciciocategoria_delete"),
    #path("tema/create/", views.tema_create, name="tema_create"),
    #path("solucion/create/", views.solucion_create, name="solucion_create"),
]

urlpatterns += [
    path("solucion/create/", views.SolucionCreate.as_view(), name="solucion_create"),
    path("solucion/list/", views.SolucionList.as_view(), name="solucion_list"),
    path("solucion/detail/<int:pk>/", views.SolucionDetail.as_view(), name="solucion_detail"),
    path("solucion/update/<int:pk>/", views.SolucionUpdate.as_view(), name="solucion_update"),
    path("solucion/delete/<int:pk>/", views.SolucionDelete.as_view(), name="solucion_delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)