from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vehiculo, Empresa
from .forms import EmpresaForm, VehiculoForm

# Vistas existentes
def home(request):
    vehiculos = Vehiculo.objects.filter(disponible=True).order_by('-fecha_ingreso')[:6]
    empresas = Empresa.objects.all()
    return render(request, 'vehiculos/home.html', {
        'vehiculos': vehiculos,
        'empresas': empresas,
    })

def lista_vehiculos(request):
    vehiculos = Vehiculo.objects.all().order_by('-fecha_ingreso')
    return render(request, 'vehiculos/lista_vehiculos.html', {
        'vehiculos': vehiculos,
        'tipos': Vehiculo.TIPO_CHOICES,
        'empresas': Empresa.objects.all(),
    })

def detalle_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    vehiculos_relacionados = Vehiculo.objects.filter(
        empresa=vehiculo.empresa
    ).exclude(id=vehiculo.id)[:3]
    
    return render(request, 'vehiculos/detalle_vehiculo.html', {
        'vehiculo': vehiculo,
        'vehiculos_relacionados': vehiculos_relacionados,
    })

def lista_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'vehiculos/lista_empresas.html', {
        'empresas': empresas,
    })

def vehiculos_por_empresa(request, empresa_id):
    empresa = get_object_or_404(Empresa, id=empresa_id)
    vehiculos = Vehiculo.objects.filter(empresa=empresa)
    
    return render(request, 'vehiculos/vehiculos_por_empresa.html', {
        'empresa': empresa,
        'vehiculos': vehiculos,
    })

def buscar_vehiculos(request):
    query = request.GET.get('q', '')
    tipo = request.GET.get('tipo', '')
    empresa_id = request.GET.get('empresa', '')
    
    vehiculos = Vehiculo.objects.filter(disponible=True)
    
    if query:
        vehiculos = vehiculos.filter(modelo__icontains=query)
    
    if tipo and tipo != 'Todos':
        vehiculos = vehiculos.filter(tipo=tipo)
        
    if empresa_id:
        vehiculos = vehiculos.filter(empresa_id=empresa_id)
    
    return render(request, 'vehiculos/buscar_vehiculos.html', {
        'vehiculos': vehiculos,
        'query': query,
        'tipo': tipo,
        'empresa_id': empresa_id,
        'tipos': Vehiculo.TIPO_CHOICES,
        'empresas': Empresa.objects.all(),
    })

# Nuevas vistas CRUD para Empresa
class EmpresaCreateView(CreateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'vehiculos/empresa_form.html'
    success_url = reverse_lazy('lista_empresas')

class EmpresaUpdateView(UpdateView):
    model = Empresa
    form_class = EmpresaForm
    template_name = 'vehiculos/empresa_form.html'
    
    def get_success_url(self):
        return reverse('vehiculos_por_empresa', kwargs={'empresa_id': self.object.id})

class EmpresaDeleteView(DeleteView):
    model = Empresa
    template_name = 'vehiculos/empresa_confirm_delete.html'
    success_url = reverse_lazy('lista_empresas')

# Nuevas vistas CRUD para Vehículo
class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculos/vehiculo_form.html'
    success_url = reverse_lazy('lista_vehiculos')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Si venimos de una empresa específica, preseleccionamos esa empresa
        empresa_id = self.kwargs.get('empresa_id')
        if empresa_id:
            form.initial['empresa'] = empresa_id
        return form

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculos/vehiculo_form.html'
    
    def get_success_url(self):
        return reverse('detalle_vehiculo', kwargs={'vehiculo_id': self.object.id})

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'vehiculos/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('lista_vehiculos')
