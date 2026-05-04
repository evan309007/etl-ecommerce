# etl.py
import json
from datetime import datetime
from app import app, db
from models import Usuario, Producto, Orden, OrdenItem, ReporteETL, MetricasDiarias

def ejecutar_etl():
    with app.app_context():
        print("=" * 50)
        print(f"🚀 INICIANDO ETL - {datetime.now()}")
        print("=" * 50)
        
        # ============ 1. EXTRACT ============
        print("\n📥 EXTRACT: Obteniendo datos...")
        
        usuarios = Usuario.query.all()
        productos = Producto.query.all()
        ordenes = Orden.query.all()
        items_orden = OrdenItem.query.all()
        
        # ============ 2. TRANSFORM ============
        print("\n🔄 TRANSFORM: Calculando métricas...")
        
        total_ventas = sum(o.total for o in ordenes)
        
        # Productos más vendidos
        ventas_productos = {}
        for item in items_orden:
            nombre = item.producto.nombre
            ventas_productos[nombre] = ventas_productos.get(nombre, 0) + item.cantidad
        
        top_productos = sorted(ventas_productos.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # Stock bajo
        stock_bajo = [(p.nombre, p.stock) for p in productos if p.stock < 5]
        
        # Ventas por mes
        ventas_por_mes = {}
        for orden in ordenes:
            mes = orden.fecha.strftime('%Y-%m')
            ventas_por_mes[mes] = ventas_por_mes.get(mes, 0) + orden.total
        
        # Usuarios por rol
        admin_count = sum(1 for u in usuarios if u.es_admin)
        
        # ============ TOP COMPRADORES (NUEVO) ============
        top_usuarios = {}
        for orden in ordenes:
            nombre_usuario = orden.usuario.nombre
            top_usuarios[nombre_usuario] = top_usuarios.get(nombre_usuario, 0) + orden.total
        
        top_compradores = sorted(top_usuarios.items(), key=lambda x: x[1], reverse=True)[:5]
        
        # ============ 3. LOAD ============
        print("\n💾 LOAD: Guardando reportes...")
        
        # Reporte de ventas (con top_compradores)
        reporte_ventas = ReporteETL(
            tipo_reporte='ventas',
            datos=json.dumps({
                'total_ventas': total_ventas,
                'total_ordenes': len(ordenes),
                'promedio_venta': total_ventas / len(ordenes) if ordenes else 0,
                'ventas_por_mes': ventas_por_mes,
                'top_compradores': top_compradores  # NUEVO
            }),
            resumen=f"Total ventas: ${total_ventas:.2f} en {len(ordenes)} órdenes"
        )
        db.session.add(reporte_ventas)
        
        # Reporte de productos
        reporte_productos = ReporteETL(
            tipo_reporte='productos',
            datos=json.dumps({
                'total_productos': len(productos),
                'top_mas_vendidos': top_productos,
                'stock_bajo': stock_bajo,
                'stock_total': sum(p.stock for p in productos)
            }),
            resumen=f"{len(productos)} productos, {len(stock_bajo)} con stock bajo"
        )
        db.session.add(reporte_productos)
        
        # Reporte de usuarios
        reporte_usuarios = ReporteETL(
            tipo_reporte='usuarios',
            datos=json.dumps({
                'total_usuarios': len(usuarios),
                'administradores': admin_count,
                'usuarios_normales': len(usuarios) - admin_count
            }),
            resumen=f"{len(usuarios)} usuarios totales"
        )
        db.session.add(reporte_usuarios)
        
        db.session.commit()
        
        # ============ 4. RESULTADOS ============
        print("\n📊 RESULTADOS:")
        print("-" * 30)
        print(f"💰 Total ventas: ${total_ventas:,.2f}")
        print(f"📦 Total productos: {len(productos)}")
        print(f"👥 Total usuarios: {len(usuarios)}")
        print(f"🏆 Top comprador: {top_compradores[0][0] if top_compradores else 'Ninguno'}")
        print(f"⚠️ Stock bajo: {len(stock_bajo)} productos")
        
        print("\n✅ ETL COMPLETADO")
        
        return True

if __name__ == '__main__':
    ejecutar_etl()