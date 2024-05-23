from django.contrib import admin
from . import models

admin.site.register(models.Ciclo)
admin.site.register(models.Profesor)
admin.site.register(models.Curso)
admin.site.register(models.Tema)

admin.site.site_title = 'Ejercicios'

class EjercicioCategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'enunciado', 'tema')
    list_display_links = ('id', 'enunciado')

class SolucionAdmin(admin.ModelAdmin):
    list_display = (
        'solucion',
        'ejercicio_id',
        'fecha_creacion',
        'imagen'
    )
    list_display_links = ('solucion', 'ejercicio_id')
    search_fields = ('solucion', 'ejercicio_id__enunciado')  # Buscar por enunciado del ejercicio
    ordering = ('ejercicio_id__id', 'solucion')  # Ordenar por ID del ejercicio
    list_filter = ('ejercicio_id__tema__nombre',)  # Filtrar por tema del ejercicio
    date_hierarchy = 'fecha_creacion'

admin.site.register(models.EjercicioCategoria, EjercicioCategoriaAdmin)
admin.site.register(models.Solucion, SolucionAdmin)