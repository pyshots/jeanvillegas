from django.contrib import admin
from . import models

admin.site.register(models.Ciclo)
admin.site.register(models.Profesor)
admin.site.register(models.Curso)
admin.site.register(models.Tema)

admin.site.site_title = 'Ejercicios'

class EjercicioCategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'enunciado',
        'tema',
        'fecha_creacion',
        'imagen_preview'
    )
    list_display_links = ('id', 'enunciado')
    search_fields = ('enunciado', 'tema__nombre')  # Buscar por enunciado y nombre del tema
    ordering = ('id',)  # Ordenar por ID del ejercicio
    list_filter = ('tema__nombre',)  # Filtrar por nombre del tema
    date_hierarchy = 'fecha_creacion'  # Jerarquía de fechas

    def imagen_preview(self, obj):
        return obj.imagen.url if obj.imagen else 'N/A'
    imagen_preview.short_description = 'Imagen'

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