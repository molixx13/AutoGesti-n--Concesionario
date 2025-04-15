from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Vistas existentes
    path('', views.home, name='home'),
    path('vehiculos/', views.lista_vehiculos, name='lista_vehiculos'),
    path('vehiculos/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('empresas/', views.lista_empresas, name='lista_empresas'),
    path('empresas/<int:empresa_id>/', views.vehiculos_por_empresa, name='vehiculos_por_empresa'),
    path('buscar/', views.buscar_vehiculos, name='buscar_vehiculos'),
    
    # Nuevas URLs para CRUD de Empresa
    path('empresas/nueva/', views.EmpresaCreateView.as_view(), name='empresa_create'),
    path('empresas/<int:pk>/editar/', views.EmpresaUpdateView.as_view(), name='empresa_update'),
    path('empresas/<int:pk>/eliminar/', views.EmpresaDeleteView.as_view(), name='empresa_delete'),
    
    # Nuevas URLs para CRUD de Vehículo
    path('vehiculos/nuevo/', views.VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('vehiculos/<int:empresa_id>/nuevo/', views.VehiculoCreateView.as_view(), name='vehiculo_create_for_empresa'),
    path('vehiculos/<int:pk>/editar/', views.VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('vehiculos/<int:pk>/eliminar/', views.VehiculoDeleteView.as_view(), name='vehiculo_delete'),
]

# Configuración para servir archivos media durante desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
