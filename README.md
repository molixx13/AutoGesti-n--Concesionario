# 🚗 AutoGestión Concesionario

Una aplicación web completa de **gestión de concesionarios de vehículos** desarrollada con Django. Sistema integral para administrar empresas concesionarias, catálogo de vehículos, búsqueda avanzada y gestión CRUD completa.

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![Django](https://img.shields.io/badge/Django-5.2-darkgreen)
![SQLite](https://img.shields.io/badge/Database-SQLite3-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Modelos de Datos](#modelos-de-datos)
- [Rutas y Vistas](#rutas-y-vistas)
- [Uso](#uso)
- [Panel de Administración](#panel-de-administración)
- [Desarrollo](#desarrollo)
- [Contribuciones](#contribuciones)

---

## ✨ Características

### 🏢 Gestión de Empresas
- ✅ Crear, editar y eliminar concesionarias
- ✅ Información completa: nombre, dirección, teléfono, email, sitio web
- ✅ Fecha de fundación y logo corporativo
- ✅ Relación uno-a-muchos con vehículos

### 🚙 Gestión de Vehículos
- ✅ Catálogo completo de vehículos disponibles
- ✅ Múltiples tipos: Sedán, SUV, Hatchback, Pickup, Deportivo, Camioneta
- ✅ Opciones de combustible: Gasolina, Diésel, Eléctrico, Híbrido, Gas
- ✅ Información detallada: modelo, año, precio, color, kilometraje
- ✅ Descarga e imágenes de vehículos
- ✅ Control de disponibilidad

### 🔍 Búsqueda y Filtrado
- ✅ Búsqueda por modelo de vehículo
- ✅ Filtrado por tipo de vehículo
- ✅ Filtrado por empresa concesionaria
- ✅ Vista de vehículos por empresa
- ✅ Vehículos relacionados en detalles

### 📊 Panel de Administración
- ✅ Interfaz admin Django integrada
- ✅ Búsqueda avanzada de registros
- ✅ Filtros por disponibilidad, tipo, combustible
- ✅ Ordenamiento por fecha de ingreso

---

## 📦 Requisitos

- **Python** 3.8 o superior
- **Django** 5.2
- **pip** (gestor de paquetes)
- **Navegador web** moderno

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/molixx13/AutoGesti-n--Concesionario.git
cd AutoGesti-n--Concesionario
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install django pillow
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear superusuario (administrador)

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para ingresar:
- Nombre de usuario
- Email
- Contraseña

### 6. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en: **http://localhost:8000**

---

## ⚙️ Configuración

### Configuración Principal (`concesionario/settings.py`)

```python
# Zona horaria (Configurado para España)
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'Europe/Madrid'

# Base de datos SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vehiculos',  # Aplicación principal
]

# Archivos estáticos y media
STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

## 🗂️ Estructura del Proyecto

```
AutoGesti-n--Concesionario/
│
├── concesionario/              # Configuración del proyecto Django
│   ├── __init__.py
│   ├── settings.py             # Configuración principal
│   ├── urls.py                 # Rutas principales
│   ├── asgi.py                 # Interfaz ASGI
│   └── wsgi.py                 # Interfaz WSGI
│
├── vehiculos/                  # Aplicación principal
│   ├── migrations/             # Migraciones de base de datos
│   ├── __init__.py
│   ├── admin.py                # Configuración del panel admin
│   ├── apps.py                 # Configuración de la aplicación
│   ├── forms.py                # Formularios Django
│   ├── models.py               # Modelos de datos
│   ├── tests.py                # Tests unitarios
│   ├── urls.py                 # Rutas de la aplicación
│   └── views.py                # Vistas (lógica de negocio)
│
├── templates/                  # Plantillas HTML
│   └── vehiculos/
│       ├── home.html
│       ├── lista_vehiculos.html
│       ├── detalle_vehiculo.html
│       ├── lista_empresas.html
│       ├── vehiculos_por_empresa.html
│       ├── buscar_vehiculos.html
│       ├── empresa_form.html
│       ├── vehiculo_form.html
│       ├── empresa_confirm_delete.html
│       └── vehiculo_confirm_delete.html
│
├── static/                     # Archivos estáticos (CSS, JS, imágenes)
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                      # Archivos cargados por usuarios
│   ├── logos/
│   └── vehiculos/
│
├── db.sqlite3                  # Base de datos SQLite
├── manage.py                   # Script de gestión Django
└── README.md                   # Este archivo
```

---

## 📊 Modelos de Datos

### Modelo: Empresa

Representa las concesionarias de vehículos.

```python
class Empresa(models.Model):
    nombre              # CharField(100)          - Nombre de la empresa
    direccion           # CharField(200)          - Dirección física
    telefono            # CharField(20)           - Número de teléfono
    email               # EmailField()            - Correo electrónico
    sitio_web           # URLField()              - Página web (opcional)
    fecha_fundacion     # DateField()             - Fecha de fundación (opcional)
    logo                # ImageField()            - Logo corporativo (opcional)
```

**Relaciones:**
- Relación uno-a-muchos con `Vehiculo` (una empresa puede tener múltiples vehículos)

---

### Modelo: Vehiculo

Representa los vehículos en el catálogo.

```python
class Vehiculo(models.Model):
    empresa             # ForeignKey(Empresa)     - Empresa propietaria
    modelo              # CharField(100)          - Modelo del vehículo
    año                 # IntegerField()          - Año de fabricación
    precio              # DecimalField(12,2)      - Precio en euros
    tipo                # CharField(20)           - Tipo de vehículo
    combustible         # CharField(20)           - Tipo de combustible
    color               # CharField(50)           - Color
    kilometraje         # IntegerField()          - Kilómetros
    descripcion         # TextField()             - Descripción (opcional)
    disponible          # BooleanField()          - Disponibilidad
    fecha_ingreso       # DateField()             - Fecha de ingreso (automática)
    imagen              # ImageField()            - Foto del vehículo (opcional)
```

**Opciones de Tipo:**
- Sedán, SUV, Hatchback, Pickup, Deportivo, Camioneta, Otro

**Opciones de Combustible:**
- Gasolina, Diésel, Eléctrico, Híbrido, Gas

---

## 🛣️ Rutas y Vistas

### Vistas de Inicio

| Ruta | Vista | Descripción |
|------|-------|-------------|
| `/` | `home` | Página de inicio con últimos vehículos disponibles |
| `/vehiculos/` | `lista_vehiculos` | Listado completo de vehículos |
| `/vehiculos/<id>/` | `detalle_vehiculo` | Detalle de un vehículo específico |

### Vistas de Empresas

| Ruta | Vista | Descripción |
|------|-------|-------------|
| `/empresas/` | `lista_empresas` | Listado de todas las empresas |
| `/empresas/<id>/` | `vehiculos_por_empresa` | Vehículos de una empresa específica |
| `/empresas/nueva/` | `EmpresaCreateView` | Crear nueva empresa |
| `/empresas/<id>/editar/` | `EmpresaUpdateView` | Editar empresa |
| `/empresas/<id>/eliminar/` | `EmpresaDeleteView` | Eliminar empresa |

### Vistas de Vehículos

| Ruta | Vista | Descripción |
|------|-------|-------------|
| `/vehiculos/nuevo/` | `VehiculoCreateView` | Crear nuevo vehículo |
| `/vehiculos/<empresa_id>/nuevo/` | `VehiculoCreateView` | Crear vehículo para empresa específica |
| `/vehiculos/<id>/editar/` | `VehiculoUpdateView` | Editar vehículo |
| `/vehiculos/<id>/eliminar/` | `VehiculoDeleteView` | Eliminar vehículo |

### Búsqueda

| Ruta | Método | Parámetros | Descripción |
|------|--------|-----------|-------------|
| `/buscar/` | GET | `q`, `tipo`, `empresa` | Búsqueda y filtrado avanzado |

**Ejemplo de búsqueda:**
```
http://localhost:8000/buscar/?q=Toyota&tipo=SUV&empresa=1
```

---

## 💻 Uso

### Acceder al Panel de Administración

1. Dirigirse a: `http://localhost:8000/admin/`
2. Iniciar sesión con el superusuario creado
3. Gestionar empresas y vehículos desde la interfaz

### Crear una Empresa

1. En el admin, seleccionar "Empresas" → "Agregar"
2. Completar los campos requeridos
3. Opcionalmente subir logo
4. Guardar

### Crear un Vehículo

1. En el admin, seleccionar "Vehículos" → "Agregar"
2. Seleccionar la empresa asociada
3. Completar datos del vehículo
4. Opcionalmente subir imagen
5. Guardar

### Buscar Vehículos

1. Navegar a `/vehiculos/` para ver todos
2. Usar `/buscar/` para filtros avanzados
3. Filtrar por modelo, tipo o empresa
4. Hacer clic en un vehículo para ver detalles

---

## 👨‍💼 Panel de Administración

### Acceso

```
URL: http://localhost:8000/admin/
Usuario: (El que creaste con createsuperuser)
```

### Funcionalidades

**Empresas:**
- ✅ Búsqueda por nombre y email
- ✅ Filtrado por fecha de fundación
- ✅ Gestión completa (CRUD)

**Vehículos:**
- ✅ Búsqueda por modelo y descripción
- ✅ Filtrado por disponibilidad, tipo, combustible, empresa
- ✅ Ordenamiento automático por fecha de ingreso
- ✅ Gestión completa (CRUD)

---

## 🔧 Desarrollo

### Crear nuevas migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### Ejecutar tests

```bash
python manage.py test
```

### Recolectar archivos estáticos (producción)

```bash
python manage.py collectstatic
```

### Shell interactivo de Django

```bash
python manage.py shell
```

Ejemplo de uso:

```python
from vehiculos.models import Empresa, Vehiculo

# Crear empresa
empresa = Empresa.objects.create(
    nombre="Mi Concesionario",
    direccion="Calle Principal 123",
    email="info@concesionario.com"
)

# Crear vehículo
vehiculo = Vehiculo.objects.create(
    empresa=empresa,
    modelo="Toyota Corolla",
    año=2024,
    precio=25000.00,
    tipo="Sedan",
    combustible="Gasolina"
)

# Consultar
print(vehiculo)  # Toyota 2024 Corolla
```

---

## 🔒 Seguridad

**⚠️ IMPORTANTE PARA PRODUCCIÓN:**

1. Cambiar `DEBUG = False` en `settings.py`
2. Generar nueva `SECRET_KEY` segura
3. Configurar `ALLOWED_HOSTS` con dominios reales
4. Usar base de datos PostgreSQL en lugar de SQLite
5. Implementar HTTPS
6. Configurar variables de entorno para datos sensibles

Ejemplo con variables de entorno:

```python
import os
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')
```

---

## 📋 Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|----------|
| Python | 3.8+ | Lenguaje de programación |
| Django | 5.2 | Framework web |
| SQLite3 | - | Base de datos |
| HTML5 | - | Estructura web |
| CSS3 | - | Estilos |
| JavaScript | - | Interactividad |
| Pillow | - | Procesamiento de imágenes |

---

## 📝 Composición del Código

- **Python:** 97.5%
- **HTML:** 1%
- **JavaScript:** 0.7%
- **CSS:** 0.6%
- **PowerShell:** 0.2%

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para grandes cambios:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👤 Autor

**molixx13** - [GitHub](https://github.com/molixx13)

---

## 📞 Soporte

Para reportar bugs o solicitar features, abre un [Issue](https://github.com/molixx13/AutoGesti-n--Concesionario/issues) en el repositorio.

---

## 🎯 Próximas Mejoras

- [ ] Sistema de login/autenticación de usuarios
- [ ] Carrito de compras
- [ ] Sistema de ofertas y descuentos
- [ ] Reportes en PDF
- [ ] API REST
- [ ] Interfaz móvil responsiva mejorada
- [ ] Sistema de comentarios/reseñas
- [ ] Integración con pasarela de pago

---

<div align="center">

**Hecho con ❤️ usando Django**

⭐ Si te gustó este proyecto, por favor déjame una estrella en GitHub

</div>
