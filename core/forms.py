from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Empleado
from django import forms

from .models import Receta, Producto

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['id_receta', 'nombre_receta', 'producto_receta', 'producto2_receta', 'producto3_receta', 'producto4_receta', 'valor_receta']

class empleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre_producto', 'detalle_producto', 'cantidad_disponible', 'fecha_compra', 'valor_unitario']
        widgets = {
            'fecha_compra': forms.DateTimeInput(format="%a %b %d %H:%M",attrs={'readonly': 'readonly'}),
        }