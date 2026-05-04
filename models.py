from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
import json

db = SQLAlchemy()

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    celular = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    es_admin = db.Column(db.Boolean, default=False)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, nombre, usuario, celular, email, password_hash, es_admin=False):
        self.nombre = nombre
        self.usuario = usuario
        self.celular = celular
        self.email = email
        self.password_hash = password_hash
        self.es_admin = es_admin
    
    def __repr__(self):
        return f'<Usuario {self.usuario}>'
    
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)
    imagen_url = db.Column(db.String(500))
    categoria = db.Column(db.String(100))
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    # Método especial para que al imprimir un producto se vea bonito
    def __repr__(self):
        return f'<Producto {self.nombre}>'    
    
class CarritoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, default=1)
    usuario = db.relationship('Usuario', backref='carrito_items')
    producto = db.relationship('Producto')
    
    # Modelo para la orden de compra
class Orden(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)
    estado = db.Column(db.String(50), default='pendiente')  # pendiente, pagado, enviado, entregado
    
    # Relación con el usuario
    usuario = db.relationship('Usuario', backref='ordenes')
    
    def __repr__(self):
        return f'<Orden {self.id} - Usuario {self.usuario_id}>'

# Modelo para cada item dentro de una orden
class OrdenItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    orden_id = db.Column(db.Integer, db.ForeignKey('orden.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_unitario = db.Column(db.Float, nullable=False)  # Precio al momento de la compra
    
    # Relaciones
    orden = db.relationship('Orden', backref='items')
    producto = db.relationship('Producto')
    
    def __repr__(self):
        return f'<OrdenItem Orden={self.orden_id} Producto={self.producto_id}>'
    
    def __repr__(self):
        return f'<CarritoItem usuario={self.usuario_id} producto={self.producto_id}>'    
    
    
    # ============ MODELOS ETL (Agregar al final) ============

class ReporteETL(db.Model):
    """Almacena los resultados de las ejecuciones ETL"""
    id = db.Column(db.Integer, primary_key=True)
    fecha_reporte = db.Column(db.DateTime, default=datetime.utcnow)
    tipo_reporte = db.Column(db.String(100))  # ventas, productos, usuarios
    datos = db.Column(db.Text)  # Guardamos JSON como texto
    resumen = db.Column(db.String(500))
    
    def get_datos(self):
        """Convierte el JSON almacenado en diccionario"""
        import json
        return json.loads(self.datos) if self.datos else {}
    
    def __repr__(self):
        return f'<ReporteETL {self.tipo_reporte} - {self.fecha_reporte}>'


class MetricasDiarias(db.Model):
    """Métricas agregadas por día para análisis rápido"""
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, unique=True, nullable=False)
    total_ventas = db.Column(db.Float, default=0)
    total_ordenes = db.Column(db.Integer, default=0)
    productos_vendidos = db.Column(db.Integer, default=0)
    usuarios_nuevos = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<MetricasDiarias {self.fecha} - Ventas: ${self.total_ventas}>'
