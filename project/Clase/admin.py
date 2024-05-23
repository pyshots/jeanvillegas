from django.contrib import admin
from . import models

admin.site.register(models.Ciclo)
admin.site.register(models.Profesor)
admin.site.register(models.Curso)
admin.site.register(models.Tema)
admin.site.register(models.Solucion)

admin.site.site_title = 'Ejercicios'

class EjercicioCategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'enunciado', 'tema')
    list_display_links = ('id', 'enunciado')

admin.site.register(models.EjercicioCategoria, EjercicioCategoriaAdmin)