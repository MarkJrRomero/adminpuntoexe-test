from django.db import models #type: ignore
from apps.productos.models import Productos

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    class Meta:
        abstract=True
        
class EstadoPedido(BaseModel):
    nombre = models.CharField(max_length=300)
   
    class Meta:
        verbose_name = "Estado pedido"
        db_table = 'estado_pedido'

    def __str__(self):
        return str(self.nombre)   
    

class Cliente(BaseModel):
    cedula = models.CharField(max_length=300)
    nombre = models.CharField(max_length=300)
    telefono = models.CharField(max_length=300)
    direccion = models.CharField(max_length=300)
   
    class Meta:
        verbose_name = "Cliente"
        db_table = 'clientes'

    def __str__(self):
        return f" {self.cedula} - {self.nombre}"   
    
    
class Pedido(BaseModel):
    cliente = models.ForeignKey(Cliente,on_delete=models.PROTECT)
    estado = models.ForeignKey(EstadoPedido,on_delete=models.PROTECT)
    observaciones = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = "Pedido"
        db_table = 'cab_pedido'

    def __str__(self):
        return f"{self.cliente} - {self.estado}"
    
    
class ProductosPedido(BaseModel):
    producto = models.ForeignKey(Productos,on_delete=models.PROTECT)
    pedido = models.ForeignKey(Pedido,on_delete=models.PROTECT)
    valor = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Cuerpo pedido"
        db_table = 'cue_pedido'

    def __str__(self):
        return f"{self.producto} - {self.pedido}"