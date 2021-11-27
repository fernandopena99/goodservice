from rest_framework import viewsets, permissions
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, View
from .utils import generate_pdf
from django.http import HttpResponse, request, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .serializers import UserSerializer
from core.serializers import RolSerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm
from .forms import empleadoForm
from django.contrib import messages
from django.template import loader, Context
from .models import *
from .forms import RecetaForm, ProductoForm
from django.db import connection
import cx_Oracle
import base64


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):

    return render(request, 'index.html')

def login_view(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('home')
   else:
        form = AuthenticationForm()
   return render(request, 'login.html', { 'form': form })

def register_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'La cuenta fue creada por '+ user)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def salir_view(request):
            logout(request)
            return redirect('index')

def crear_receta(request):
    data = {
        'productos': listar_productos_receta()
    }

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        producto = request.POST.get('producto')
        producto2 = request.POST.get('producto2')
        producto3 = request.POST.get('producto3')
        producto4 = request.POST.get('producto4')
        valor = request.POST.get('valor')
        imagen = request.FILES['imagen'].read()

        salida = registrar_receta(nombre,producto, producto2, producto3, producto4,imagen,valor)
        salida2 = stock_receta(producto, producto2, producto3, producto4)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
        else:
            data['mensaje'] = 'no se ha podido registrar'

    return render(request, 'crear_receta.html', data)

def registrar_receta(nombre, producto, producto2, producto3, producto4, imagen, valor):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RECETA', [nombre,producto, producto2, producto3, producto4,imagen,valor, salida])
    return salida.getvalue()

def stock_receta(producto, producto2, producto3, producto4):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_STOCK_RECETA', [producto, producto2, producto3, producto4, salida])
    return salida.getvalue()

def listar_receta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RECETA", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def listar_productos_receta():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS_RECETA", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

    

def empleados(request):
    data = {
        'empleados': listado_empleados(),
        'rol':listar_rol(),
    }

    #agregar_empleado('floripondio','gomez','flo@gmail.com',2)

    if request.method == "POST":
        #id_empleado = request.POST.get('id_empleado')
        nombre_empleado = request.POST.get('nombre_empleado')
        apellido_empleado = request.POST.get('apellido_empleado')
        email_empleado = request.POST.get('email_empleado')
        rol_id_rol = request.POST.get('rol_id_rol')
        salida = agregar_empleado(nombre_empleado, apellido_empleado, email_empleado, rol_id_rol)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['empleados'] = listado_empleados()
        else:
            data['mensaje'] = 'no se ha podido guardar'

    return render(request, 'core/empleado.html', data)

def agregar_empleado(nombre_empleado, apellido_empleado, email_empleado, rol_id_rol):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    #llamar al procedimiento
    cursor.callproc('SP_AGREGAR_EMPLEADO', [nombre_empleado, apellido_empleado, email_empleado, rol_id_rol, salida])
    return salida.getvalue()

def listado_empleados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_EMPLEADOS", [out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def recetas(request):
    datos_receta = listar_receta()
    
    arreglo = []

    for i in datos_receta:
        data = {
            'data':i,
            'imagen':str(base64.b64encode(i[6].read()), 'utf-8')
        }
        arreglo.append(data)

    data = {
        'recetas':arreglo
    }

    return render(request, 'listar_Receta.html', data)

def mod_receta(request, id_receta):
    datos_receta = filtrar_receta(id_receta)
    
    arreglo = []

    for i in datos_receta:
        data = {
            'data':i,
            'imagen':str(base64.b64encode(i[6].read()), 'utf-8')
        }
        arreglo.append(data)

    data = {
        'recetas':arreglo,
        'productos': listar_productos_receta()
    }

    if request.method == "POST":
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        producto = request.POST.get('producto')
        producto2 = request.POST.get('producto2')
        producto3 = request.POST.get('producto3')
        producto4 = request.POST.get('producto4')
        valor = request.POST.get('valor')
        imagen = request.FILES['imagen'].read()
        salida = editarReceta(id,nombre,producto, producto2, producto3, producto4,imagen, valor)
        if salida == 1:
            data['mensaje'] = 'Datos Actualizados correctamente'
        else:
            data['mensaje'] = 'no se ha podido actualizar'

    return render(request, 'mod_receta.html', data)

def editarReceta(id, nombre, producto, producto2, producto3, producto4, imagen, valor):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_RECETA', [id,nombre,producto, producto2, producto3, producto4,imagen,valor, salida])
    return salida.getvalue()


def filtrar_receta(id_receta):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_FILTRAR_RECETA", [id_receta, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def listar_rol():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_ROL", [out_cur])
    
    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def base(request):
    return render (request, "core/base.html")


def modificar_empleado (request, id_empleado):
    data ={
        'empleados': filtrar_empleado(id_empleado),
        'rol': listar_rol()
    }

    if request.method == "POST":
        id_empleado = request.POST.get('id_empleado')
        nombre_empleado = request.POST.get('nombre_empleado')
        apellido_empleado = request.POST.get('apellido_empleado')
        email_empleado = request.POST.get('email_empleado')
        rol_id_rol = request.POST.get('rol_id_rol')
        salida = mod_empleado(id_empleado, nombre_empleado, apellido_empleado, email_empleado, rol_id_rol)
        if salida == 1:
            data['mensaje'] = 'Actualizado correctamente'
        else:
            data['mensaje'] = 'no se ha podido actualizar'
        return redirect ('empleados')
    return render(request, 'core/modificar_empleado.html', data)

def mod_empleado(id_empleado, nombre_empleado, apellido_empleado, email_empleado, rol_id_rol):
	django_cursor = connection.cursor()
	cursor = django_cursor.connection.cursor()
	salida = cursor.var(cx_Oracle.NUMBER)
	cursor.callproc('SP_ACTUALIZAR_DATOS',[id_empleado, nombre_empleado, apellido_empleado, email_empleado, rol_id_rol, salida])
	return salida.getvalue()
    
def filtrar_empleado(id_empleado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("mostrar_empleados_mod", [id_empleado, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


@login_required(login_url="/login/")
def home(request):

    return render(request, 'home.html')

def eliminar_receta(request, id_receta):

    data = {
        'recetas':listar_receta(),
        
    }

    if request.method == "GET":
        #id = request.POST.get('id')
        salida = eliminarReceta(id_receta)
        if salida == 1:
            data['mensaje'] = 'Datos Eliminados correctamente'
        else:
            data['mensaje'] = 'no se ha podido eliminar'

    return render(request, 'crear_receta.html', data)

def eliminarReceta(id_receta):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_RECETA', [id_receta, salida])
    return salida.getvalue()
    
def eliminaEmpleado(id_empleado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_EMPLEADO', [id_empleado, salida])
    return salida.getvalue()

def eliminarEmpleado(request, id_empleado):
    data = {
        'empleados': listado_empleados(),
    }
    if request.method == 'GET':
        #id_empleado = request.POST.get('id_empleado')
        salida = eliminaEmpleado(id_empleado)
        if salida == 1:
            data['mensaje'] = 'Datos Actualizados correctamente'
        else:
            data['mensaje'] = 'no se ha podido actualizar'
        return redirect ('empleados')
        
    return render(request, 'core/empleado.html', data)

#############################################################################################################

def add (request):
    
    form = empleadoForm

    if request.method =="POST":
        form = empleadoForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            return render(request,'core/base.html')
    return render(request, "core/add.html",{'form':form})


def edit(request,id_empleado):
    instancia = Empleado.objects.get(id_empleado = id_empleado)
    form = empleadoForm (instance=instancia)

    if request.method == "POST":

        form = empleadoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
    return render(request,"core/edit.html", {'form': form})

def delete (request, id_empleado):
    instancia = Empleado.objects.get(id_empleado = id_empleado)
    instancia.delete()
    return redirect ('/')


def productos(request):
    data = {
       'productos': listado_productos(),
       'empleado': listado_empleados(),
    }
    salida2 = alertaStock()
    print('Tu salida')
    print(salida2)
    if salida2 == 1:
        data['alerta']= 'Alerta'
    else:
        data['alerta']='No hay'
        
    if request.method == 'POST':
        nombre_producto = request.POST.get('nombre_producto')
        detalle_producto = request.POST.get('detalle_producto')
        cantidad_disponible = request.POST.get('cantidad_disponible')
        fecha_compra = request.POST.get('fecha_compra')
        valor_unitario= request.POST.get('valor_unitario')
        empleado_id_empleado = request.POST.get('id_empleado')
        salida = agregar_producto(nombre_producto,detalle_producto,cantidad_disponible,fecha_compra, valor_unitario,empleado_id_empleado)
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente'
            data['productos'] = listado_productos()
        else:
            data['mensaje'] = 'No se ha podido registrar'
    return render(request, 'productos.html', data)



def listado_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def agregar_producto(nombre_producto,detalle_producto,cantidad_disponible,fecha_compra, valor_unitario,empleado_id_empleado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PRODUCTO', [nombre_producto,detalle_producto,cantidad_disponible,fecha_compra, valor_unitario,empleado_id_empleado, salida])
    return salida.getvalue()

def mod_producto(request, id_producto):
    data = {
       'producto': filtrar_producto(id_producto),
       'empleado': listado_empleados(),
    }
    
    if request.method == 'POST':
        id_producto = request.POST.get('id_producto')
        print(id_producto)
        nombre_producto = request.POST.get('nombre_producto')
        print(nombre_producto)
        detalle_producto = request.POST.get('detalle_producto')
        print(detalle_producto)
        cantidad_disponible = request.POST.get('cantidad_disponible')
        print(cantidad_disponible)
        fecha_compra = request.POST.get('fecha_compra')
        print(fecha_compra)
        valor_unitario= request.POST.get('valor_unitario')
        print(valor_unitario)
        empleado_id_empleado = request.POST.get('id_empleado')
        print(empleado_id_empleado)
        salida = modificar_producto(id_producto,nombre_producto,detalle_producto,cantidad_disponible,fecha_compra, valor_unitario,empleado_id_empleado)
        if salida == 1:
            data['mensaje'] = 'Modificado correctamente'
        else:
            data['mensaje'] = 'No se ha podido modificar'
    return render(request, 'mod_producto.html', data)

def modificar_producto(id_producto,nombre_producto,detalle_producto,cantidad_disponible,fecha_compra, valor_unitario,empleado_id_empleado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_PRODUCTO', [id_producto,nombre_producto,detalle_producto,cantidad_disponible,fecha_compra, valor_unitario,empleado_id_empleado, salida])
    return salida.getvalue()



def eli_producto(request, id_producto):
    data = {
        'productos': listado_productos(),
    }
    if request.method == 'GET':
        #id_producto = request.GET.get('id_producto')
       
        salida = eliminar_producto(id_producto)
        
        if salida == 1:
            data['mensaje'] = 'Datos Actualizados correctamente'
        else:
            data['mensaje'] = 'No se ha podido actualizar'
        return redirect('productos')
    return render(request, 'productos.html', data)

def eliminar_producto(id_producto):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_PRODUCTO', [id_producto, salida])
    return salida.getvalue()

def filtrar_producto(id_producto):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_MOSTRAR_PRODUCTO_MOD", [id_producto, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


class listPedidosListView(ListView):
    model = Pedido
    template_name = 'pedidos.html'
    context_object_name = 'pedidos'

class listPedidosPdf(View):

    def get(self, request, *args, **kwargs):
        pedidos = Pedido.objects.all()
        data = {
            'pedidos': pedidos
        }
        pdf = generate_pdf('pedidosss.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def alertaStock():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("ALERTA_STOCK", [salida])
    return salida.getvalue()

class ordenesPedidos(ListView):
    model = Pedido
    template_name = 'ordenes_pedidos.html'
    context_object_name = 'pedidos'

class listPagosPdf(View):

    def get(self, request, *args, **kwargs):
        pagos = Pago.objects.all()
        data = {
            'pagos': pagos
        }
        pdf = generate_pdf('pago.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

class listPagosListView(ListView):
    model = Pago
    template_name = 'pago.html'
    context_object_name = 'pagos'