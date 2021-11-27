from django.contrib import admin
from .models import Caja,Cliente,Cocina,Empleado,Mesa,MetodoPago,Pago,Pedido,PedidoBodega,Producto,Receta,ReporteFinanzas,Rol,Servicio,AuthGroup, AuthGroupPermissions, AuthPermission, AuthUser, AuthUserGroups,AuthUserUserPermissions

# Register your models here.
admin.site.register(Caja)
admin.site.register(Cliente)
admin.site.register(Cocina)
admin.site.register(Empleado)
admin.site.register(Mesa)
admin.site.register(MetodoPago)
admin.site.register(Pago)
admin.site.register(Pedido)
admin.site.register(PedidoBodega)
admin.site.register(Producto)
admin.site.register(Receta)
admin.site.register(ReporteFinanzas)
admin.site.register(Rol)
admin.site.register(Servicio)
admin.site.register(AuthGroup)
admin.site.register(AuthGroupPermissions)
admin.site.register(AuthPermission)
admin.site.register(AuthUser)
admin.site.register(AuthUserGroups)
admin.site.register(AuthUserUserPermissions)




