from django import forms #type: ignore
from .models import *

class ProductoForm(forms.ModelForm):
 
    class Meta:
        model = Productos
        fields = ('descripcion','referencia','proveedor','costo_uni')