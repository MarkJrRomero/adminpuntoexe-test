from django.db import models
from apps.productos.models import *

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    class Meta:
        abstract=True
         
class Inventario(BaseModel):
    producto = models.ForeignKey(Productos,on_delete=models.PROTECT)
    cantidad = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Inventario"
        db_table = 'inventario_productos'

    def __str__(self):
        return str(self.producto) + ' - ' + str(self.cantidad)