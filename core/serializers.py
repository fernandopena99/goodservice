from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token   

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user
from core.models import Caja,Cliente,Cocina,Empleado,Mesa,MetodoPago,Pago,Pedido,PedidoBodega,Producto,Receta,ReporteFinanzas,Rol,Servicio
from rest_framework import serializers

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class CocinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cocina
        fields = '__all__'

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'
    
class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoBodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoBodega
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class RecetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receta
        fields = '__all__'
    
class ReporteFinanzasSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteFinanzas
        fields = '__all__'

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = '__all__'
