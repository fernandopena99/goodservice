from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import include, url
from rest_framework import routers
from django.contrib.auth.views import LoginView
from . import views
from .views import UserViewSet
from .api import *
from core import views

router = routers.DefaultRouter()
router.register('cajas', CajaViewSet, 'cajas')
router.register('clientes', ClienteViewSet, 'clientes')
router.register('cocina', CocinaViewSet, 'cocina')
router.register('empleados', EmpleadoViewSet, 'empleados')
router.register('mesas', MesaViewSet, 'mesas')
router.register('metodos-pago', MetodoPagoViewSet, 'metodos-pago')
router.register('pagos', PagoViewSet, 'pagos')
router.register('pedidos', PedidoViewSet, 'pedidos')
router.register('pedidos-bodega', PedidoBodegaViewSet, 'pedidos-bodega')
router.register('productos', ProductoViewSet, 'productos')
router.register('recetas', RecetaViewSet, 'recetas')
router.register('reportes-finanzas', ReporteFinanzasViewSet, 'reportes-finanzas')
router.register('roles', RolViewSet, 'roles')
router.register('servicios', ServicioViewSet, 'servicios')
router.register('users', UserViewSet, 'users')

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    #url(r'^login/$', LoginView.as_view(template_name='login.html'), name='Login'),
    url(r'^login/$', views.login_view, name = "login"),
    url(r'^home$', views.home, name='home'),
    url(r'^register/$', views.register_view, name = "register"),
    url(r'^Receta/$', views.crear_receta, name = "crearReceta"),
    url(r'^listar_receta/$', views.recetas, name='listarReceta'),
    url(r'^mod_receta/(?P<id_receta>\d+)/$', views.mod_receta, name='mod_receta'),
    url(r'^eliminar_Receta/(?P<id_receta>\d+)/$', views.eliminar_receta, name = "eliminar_Receta"),
#    url(r'^mod_empleado/(?P<id_empleado>\d+)/$', views.mod_empleado, name='mod_empleado'),
    url(r'^salir/$', views.salir_view, name = "salir"),
    url(r'^Productos/$', views.productos, name="productos"),
    url(r'^mod_producto/(?P<id_producto>\d+)/$', views.mod_producto, name='mod_producto'),
    url(r'^eliminar_producto/(?P<id_producto>\d+)/$', views.eli_producto, name='eli_producto'),
    path('',views.empleados, name='empleados'),
    path('base/',views.base, name="base"),
    path('base/empleados',views.empleados, name='empleados'),
    path('add',views.add, name='add'),
    path('edit/<int:id_empleado>', views.edit, name='edit'),
    path('delete/<int:id_empleado>', views.delete),
    path('apirest', include(router.urls)),
    url(r'^modificar_empleado/(?P<id_empleado>\d+)/$', views.modificar_empleado, name='modificar_empleado'),
    url(r'^eliminar_Empleado/(?P<id_empleado>\d+)/$', views.eliminarEmpleado, name = "eliminarEmpleado"),
    path('pedidos/',views.listPedidosListView.as_view(), name='pedidos'),
    path('ordenes/',views.ordenesPedidos.as_view(), name='ordenes'),
    path('pedidos-pdf/',views.listPedidosPdf.as_view(), name='pedidos_all'),
    path('pagos/',views.listPagosListView.as_view(), name='pagos'),
    path('pagos-pdf/',views.listPagosPdf.as_view(), name='pagos_all'),
]
"""  
router = routers.DefaultRouter()
router.register('api/cajas', CajaViewSet, 'cajas')
router.register('api/clientes', ClienteViewSet, 'clientes')
router.register('api/cocina', CocinaViewSet, 'cocina')
router.register('api/empleados', EmpleadoViewSet, 'empleados')
router.register('api/mesas', MesaViewSet, 'mesas')
router.register('api/metodos-pago', MetodoPagoViewSet, 'metodos-pago')
router.register('api/pagos', PagoViewSet, 'pagos')
router.register('api/pedidos', PedidoViewSet, 'pedidos')
router.register('api/pedidos-bodega', PedidoBodegaViewSet, 'pedidos-bodega')
router.register('api/productos', ProductoViewSet, 'productos')
router.register('api/recetas', RecetaViewSet, 'recetas')
router.register('api/reportes-finanzas', ReporteFinanzasViewSet, 'reportes-finanzas')
router.register('api/roles', RolViewSet, 'roles')
router.register('api/servicios', ServicioViewSet, 'servicios')
"""
