# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClienteReciclador(models.Model):
    idreciclador = models.UUIDField(primary_key=True)
    username = models.CharField(max_length=70)
    contrasena = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    nombre = models.CharField(max_length=70)
    direccion = models.CharField(max_length=100)
    recipuntos = models.IntegerField(blank=True, null=True)
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cliente_reciclador'
        unique_together = (('username', 'email'),)


class DetalleTransaccionCompra(models.Model):
    id = models.UUIDField(primary_key=True)
    cantproducto = models.IntegerField()
    totalrecipuntosdetalle = models.IntegerField()
    idtransaccioncompra = models.ForeignKey('TransaccionCompra', models.DO_NOTHING, db_column='idtransaccioncompra')
    idproducto = models.ForeignKey('ProductoDePrimeraNecesidad', models.DO_NOTHING, db_column='idproducto')

    class Meta:
        managed = False
        db_table = 'detalle_transaccion_compra'


class DetalleTransaccionVenta(models.Model):
    id = models.UUIDField(primary_key=True)
    cantproducto = models.IntegerField()
    totalrecipuntosdetalle = models.IntegerField()
    idtransaccionventa = models.ForeignKey('TransaccionVenta', models.DO_NOTHING, db_column='idtransaccionventa')
    idreciclaje = models.ForeignKey('ProductoDeReciclaje', models.DO_NOTHING, db_column='idreciclaje')

    class Meta:
        managed = False
        db_table = 'detalle_transaccion_venta'



class Domiciliario(models.Model):
    iddomiciliario = models.UUIDField(primary_key=True)
    username = models.CharField(max_length=70)
    contraseña = models.CharField(max_length=20)
    nombre = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    cedula = models.BigIntegerField()
    tipovehiculo = models.CharField(max_length=40, blank=True, null=True)
    cantomicilios = models.IntegerField()
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'domiciliario'
        unique_together = (('username', 'nombre', 'cedula', 'email'),)


class Pago(models.Model):
    idpago = models.UUIDField(primary_key=True)
    mes = models.IntegerField()
    año = models.IntegerField()
    valorpago = models.DecimalField(max_digits=10, decimal_places=2)
    totalrecipuntos = models.IntegerField()
    iddomiciliario = models.ForeignKey(Domiciliario, models.DO_NOTHING, db_column='iddomiciliario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'
        unique_together = (('mes', 'año'),)


class ProductoDePrimeraNecesidad(models.Model):
    idproducto = models.UUIDField(primary_key=True)
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=2000, blank=True, null=True)
    dirimagen = models.CharField(max_length=100)
    preciopesos = models.DecimalField(max_digits=10, decimal_places=2)
    recipuntosporgramos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producto_de_primera_necesidad'


class ProductoDeReciclaje(models.Model):
    idreciclaje = models.UUIDField(primary_key=True)
    nombre = models.CharField(max_length=70)
    descripción = models.CharField(max_length=2000, blank=True, null=True)
    dirimagen = models.CharField(max_length=100)
    preciopesos = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    recipuntosporgamo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'producto_de_reciclaje'


class TablaPagos(models.Model):
    minrecipuntos = models.IntegerField(primary_key=True)
    maxrecipuntos = models.IntegerField()
    pago = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tabla_pagos'
        unique_together = (('minrecipuntos', 'maxrecipuntos'),)


class TransaccionCompra(models.Model):
    idtransaccioncompra = models.UUIDField(primary_key=True)
    totalrecipuntostransaccion = models.IntegerField()
    fecha = models.DateTimeField()
    idreciclador = models.ForeignKey(ClienteReciclador, models.DO_NOTHING, db_column='idreciclador')
    iddomiciliario = models.ForeignKey(Domiciliario, models.DO_NOTHING, db_column='iddomiciliario')
    idpago = models.ForeignKey(Pago, models.DO_NOTHING, db_column='idpago')

    class Meta:
        managed = False
        db_table = 'transaccion_compra'


class TransaccionVenta(models.Model):
    idtransaccionventa = models.UUIDField(primary_key=True)
    totalrecipuntostransaccion = models.IntegerField()
    fecha = models.DateTimeField()
    idreciclador = models.ForeignKey(ClienteReciclador, models.DO_NOTHING, db_column='idreciclador')
    iddomiciliario = models.ForeignKey(Domiciliario, models.DO_NOTHING, db_column='iddomiciliario')
    idpago = models.ForeignKey(Pago, models.DO_NOTHING, db_column='idpago')

    class Meta:
        managed = False
        db_table = 'transaccion_venta'
