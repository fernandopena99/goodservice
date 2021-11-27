from core.models import *
from rest_framework import viewsets, permissions
from .serializers import *

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    permission_classes = [permissions.AllowAny]

class CajaViewSet(viewsets.ModelViewSet):
    queryset = Caja.objects.all()
    serializer_class = CajaSerializer
    permission_classes = [permissions.AllowAny]

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.AllowAny]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.AllowAny]

class CocinaViewSet(viewsets.ModelViewSet):
    queryset = Cocina.objects.all()
    serializer_class = Cocina
    permission_classes = [permissions.AllowAny]

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    permission_classes = [permissions.AllowAny]

class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer
    permission_classes = [permissions.AllowAny]

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [permissions.AllowAny]

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.AllowAny]

class PedidoBodegaViewSet(viewsets.ModelViewSet):
    queryset = PedidoBodega.objects.all()
    serializer_class = PedidoBodegaSerializer
    permission_classes = [permissions.AllowAny]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.AllowAny]

class RecetaViewSet(viewsets.ModelViewSet):
    queryset = Receta.objects.all()
    serializer_class = RecetaSerializer
    permission_classes = [permissions.AllowAny]

class ReporteFinanzasViewSet(viewsets.ModelViewSet):
    queryset = ReporteFinanzas.objects.all()
    serializer_class = ReporteFinanzasSerializer
    permission_classes = [permissions.AllowAny]

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    permission_classes = [permissions.AllowAny]

