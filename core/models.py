# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Caja(models.Model):
    id_caja = models.FloatField(primary_key=True)
    fecha_operacion = models.DateField()
    monto_ingreso = models.IntegerField()
    monto_egreso = models.IntegerField()
    estado_caja = models.CharField(max_length=30)
    empleado_id_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='empleado_id_empleado')

    class Meta:
        managed = False
        db_table = 'caja'
    
    def __str__(self):
        return self.estado_caja


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre_cliente = models.CharField(max_length=30)
    mesa_id_mesa = models.ForeignKey('Mesa', models.DO_NOTHING, db_column='mesa_id_mesa')

    class Meta:
        managed = False
        db_table = 'cliente'

    def __str__(self):
        return self.nombre_cliente


class Cocina(models.Model):
    id_cocina = models.FloatField(primary_key=True)
    estado = models.CharField(max_length=30)
    empleado_id_empleado = models.ForeignKey('Empleado', models.DO_NOTHING, db_column='empleado_id_empleado')
    pedido_id_pedido = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedido_id_pedido', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cocina'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    id_empleado = models.FloatField(primary_key=True)
    nombre_empleado = models.CharField(max_length=30)
    apellido_empleado = models.CharField(max_length=30)
    email_empleado = models.CharField(max_length=30)
    rol_id_rol = models.ForeignKey('Rol', models.DO_NOTHING, db_column='rol_id_rol')

    class Meta:
        managed = False
        db_table = 'empleado'


class Mesa(models.Model):
    id_mesa = models.FloatField(primary_key=True)
    nro_mesa = models.IntegerField()
    capacidad_mesa = models.IntegerField()
    cantidad_clientes = models.IntegerField()
    estado = models.CharField(max_length=30)
    hora_inicio = models.DateField(blank=True, null=True)
    hora_termino = models.DateField(blank=True, null=True)
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')

    class Meta:
        managed = False
        db_table = 'mesa'


class MetodoPago(models.Model):
    id_metodo_pago = models.FloatField(primary_key=True)
    nombre_metodo_pago = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'metodo_pago'
    
    def __str__(self):
        return self.nombre_metodo_pago


class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    monto_pago = models.IntegerField()
    metodo_pago_id_metodo_pago = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='metodo_pago_id_metodo_pago')
    caja_id_caja = models.ForeignKey(Caja, models.DO_NOTHING, db_column='caja_id_caja')

    class Meta:
        managed = False
        db_table = 'pago'


class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    estado = models.CharField(max_length=30)
    detalle = models.CharField(max_length=120, blank=True, null=True)
    fecha_creacion = models.CharField(max_length=30)
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    receta_id_receta = models.ForeignKey('Receta', models.DO_NOTHING, db_column='receta_id_receta')

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoBodega(models.Model):
    id_pedido_bodega = models.FloatField(primary_key=True)
    fecha_pedido = models.DateField(blank=True, null=True)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=30)
    valor_pedido = models.IntegerField()
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')
    producto_id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='producto_id_producto', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedido_bodega'


class Producto(models.Model):
    id_producto = models.FloatField(primary_key=True)
    nombre_producto = models.CharField(max_length=30)
    detalle_producto = models.CharField(max_length=120)
    cantidad_disponible = models.IntegerField()
    fecha_compra = models.DateField(blank=True, null=True)
    valor_unitario = models.IntegerField()
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')

    class Meta:
        managed = False
        db_table = 'producto'


class Receta(models.Model):
    id_receta = models.FloatField(primary_key=True)
    nombre_receta = models.CharField(max_length=60)
    producto_receta = models.CharField(max_length=120)
    producto2_receta = models.CharField(max_length=120)
    producto3_receta = models.CharField(max_length=120)
    producto4_receta = models.CharField(max_length=120)
    imagen_receta = models.BinaryField(blank=True, null=True)
    valor_receta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'receta'

    def __str__(self):
        return self.nombre_receta


class ReporteFinanzas(models.Model):
    id_reporte = models.FloatField(primary_key=True)
    fecha_creacion = models.DateField()
    monto_total = models.IntegerField()
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')

    class Meta:
        managed = False
        db_table = 'reporte_finanzas'


class Rol(models.Model):
    id_rol = models.FloatField(primary_key=True)
    nombre_rol = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'rol'


class Servicio(models.Model):
    id_servicio = models.FloatField(primary_key=True)
    hora_inicio = models.DateField(blank=True, null=True)
    hora_termino = models.DateField(blank=True, null=True)
    cantidad_clientes = models.IntegerField()
    mesa_id_mesa = models.ForeignKey(Mesa, models.DO_NOTHING, db_column='mesa_id_mesa')
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    empleado_id_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_empleado')
    pago_id_pago = models.ForeignKey(Pago, models.DO_NOTHING, db_column='pago_id_pago', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servicio'
        unique_together = (('id_servicio', 'mesa_id_mesa'),)
