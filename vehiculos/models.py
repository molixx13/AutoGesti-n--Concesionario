from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    sitio_web = models.URLField(blank=True, null=True)
    fecha_fundacion = models.DateField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

class Vehiculo(models.Model):
    TIPO_CHOICES = [
        ('Sedan', 'Sedán'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
        ('Pickup', 'Pickup'),
        ('Deportivo', 'Deportivo'),
        ('Camioneta', 'Camioneta'),
        ('Otro', 'Otro'),
    ]
    
    COMBUSTIBLE_CHOICES = [
        ('Gasolina', 'Gasolina'),
        ('Diesel', 'Diésel'),
        ('Eléctrico', 'Eléctrico'),
        ('Híbrido', 'Híbrido'),
        ('Gas', 'Gas'),
    ]
    
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='vehiculos')
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    combustible = models.CharField(max_length=20, choices=COMBUSTIBLE_CHOICES)
    color = models.CharField(max_length=50)
    kilometraje = models.IntegerField(default=0)
    descripcion = models.TextField(blank=True, null=True)
    disponible = models.BooleanField(default=True)
    fecha_ingreso = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='vehiculos/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.empresa} {self.modelo} ({self.año})"
    
    class Meta:
        verbose_name = 'Vehículo'
        verbose_name_plural = 'Vehículos'
