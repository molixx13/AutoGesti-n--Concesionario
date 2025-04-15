from django.contrib import admin
from .models import Empresa, Vehiculo

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono', 'email', 'sitio_web')
    search_fields = ('nombre', 'email')
    list_filter = ('fecha_fundacion',)

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'empresa', 'año', 'precio', 'tipo', 'combustible', 'color', 'disponible')
    list_filter = ('disponible', 'tipo', 'combustible', 'empresa')
    search_fields = ('modelo', 'descripcion')
    date_hierarchy = 'fecha_ingreso'
