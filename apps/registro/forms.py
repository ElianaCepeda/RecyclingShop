from django.db.models import fields
from .models import *

class ClienteRecicladorForm(foms.model):
    class Meta:
        model= ClienteReciclador
        fields = "__all__"