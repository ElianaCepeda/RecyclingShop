from django.contrib import admin
from .models import *

admin.site.register(ClienteReciclador)
admin.site.register(DetalleTransaccionCompra)
admin.site.register(DetalleTransaccionVenta)
admin.site.register(Domiciliario)
admin.site.register(Pago)
admin.site.register(ProductoDePrimeraNecesidad)
admin.site.register(ProductoDeReciclaje)
admin.site.register(TablaPagos)
admin.site.register(TransaccionCompra)
admin.site.register(TransaccionVenta)