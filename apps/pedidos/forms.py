from django import forms #type: ignore
from .models import *

class PedidoForm(forms.ModelForm):
 
    class Meta:
        model = Pedido
        fields = ('cliente', 'observaciones')