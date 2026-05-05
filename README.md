# ETL Analytics para Ecommerce

Sistema CRUD (Create, Read, Update, Delete) con ETL (Extract, Transform, Load) para análisis de datos de ecommerce con Flask.

## Demo en vivo

> *Próximamente después del despliegue en Render*

## Características

###  Módulo de Ecommerce
- ✅ Autenticación de usuarios (registro/login)
- ✅ Roles (administrador / usuario normal)
- ✅ CRUD completo de productos
- ✅ Carrito de compras
- ✅ Checkout y órdenes
- ✅ Historial de compras

###  Módulo ETL
- ✅ Extracción automática de datos de ventas, productos y usuarios
- ✅ Transformación con cálculo de métricas clave
- ✅ Carga a tablas de reportes
- ✅ Dashboard interactivo con gráficos (Chart.js)
- ✅ Exportación a Excel con formato profesional

###  Dashboard ETL
- **Ventas por Mes** - Gráfico de barras con tendencia
- **Top Productos** - Productos más vendidos
- **Stock Bajo** - Alerta de inventario crítico
- **Top Compradores** - Usuarios que más gastan

###  Exportación a Excel
El Excel generado incluye **10 hojas** con formato profesional:
1. Resumen Ejecutivo (KPIs principales)
2. Ventas por Mes
3. Stock Bajo
4. Top Productos ETL
5. Usuarios (con total gastado)
6. Productos (inventario completo)
7. Órdenes (historial)
8. Detalle de Compras (items individuales)
9. Ventas por Usuario
10. Top Compradores

##  Tecnologías

| Tecnología              |                Uso          |
|-------------------------|-----------------------------|
| **Flask**               | Framework web               |
| **SQLAlchemy**          | ORM para base de datos      |
| **SQLite / PostgreSQL** | Base de datos               |
| **Flask-Login**         | Autenticación               |
| **bcrypt**              | Encriptación de contraseñas |
| **Chart.js**            | Gráficos interactivos       |
| **pandas**              | Transformación de datos     |
| **openpyxl**            | Generación de Excel         |
| **Bootstrap 5**         | Interfaz de usuario         |
| **Jinja2**              | Templates HTML              |

##  Instalación Local

### Requisitos previos
- Python 3.11 o superior
- Git

### Pasos de instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/evan309007/etl-ecommerce.git
cd etl-ecommerce

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
python app.py

      Credenciales por defecto

Rol         	Usuario	   Contraseña
Administrador	admin	   admin123



Estructura del Proyecto

etl-ecommerce/
├── app.py                    # Aplicación principal (rutas, endpoints)
├── models.py                 # Modelos de base de datos
├── etl.py                    # Script ETL (extracción, transformación y carga)
├── requirements.txt          # Dependencias del proyecto
├── README.md                 # Documentación
├── CHANGELOG.md              # Implementaciones, mejoras y correcciones
├── CONTRIBUTING.md           # Contribuciones y reportar errores
│
├── templates/                # Templates HTML
│   ├── login.html
│   ├── registro.html
│   ├── perfil.html
│   ├── productos.html
│   ├── carrito.html
│   ├── dashboard.html
│   ├── gestionar_productos.html
│   ├── mis_ordenes.html
│   ├── orden_detalle.html
│   ├── dashboard_etl.html
│   └── navbar.html           # Barra de navegación reutilizable
│
└── static/                   # Archivos estáticos
    └── style.css             # Estilos personalizados

    Uso del ETL
Ejecutar ETL manualmente
python etl.py


Ver dashboard ETL
Accede a http://localhost:5000/dashboard/etl


Exportar reporte a Excel
Desde el dashboard, haz clic en "Exportar a Excel"


🔄 Flujos Principales
1. Proceso ETL
text
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  EXTRACT    │ ──► │ TRANSFORM   │ ──► │    LOAD     │
│  (Extraer)  │     │(Transformar)│     │  (Cargar)   │
└─────────────┘     └─────────────┘     └─────────────┘
      │                    │                    │
      ▼                    ▼                    ▼
   Base de           Cálculos            Tablas de
    Datos            Métricas             Reportes



2. Exportación a Excel
text
Dashboard ETL ──► Generar Excel ──► Descargar archivo
                                    reporte_etl_*.xlsx



        Métricas Calculadas

Métrica	                 Descripción
Ventas Totales	         Suma de todas las órdenes
Promedio por Venta	     Ventas totales / Número de órdenes
Top Productos	         Productos más vendidos (unidades)
Stock Bajo	             Productos con stock < 5 unidades
Top Compradores	         Usuarios con mayor gasto total
Ventas por Mes	         Tendencia mensual
Valor Inventario	     Precio × Stock por producto



 Licencia
    MIT

Autor
carlos armando luevanos zamora - https://github.com/evan309007/etl-ecommerce.git


Agradecimientos

Flask por el excelente framework

Chart.js por los gráficos interactivos

Bootstrap por el diseño responsive