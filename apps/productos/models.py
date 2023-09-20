from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)
    class Meta:
        abstract=True
     
class Proveedor(BaseModel):
    nombre = models.CharField(max_length=300)
   
    class Meta:
        verbose_name = "Proveedor"
        db_table = 'maestro_proveedores'

    def __str__(self):
        return str(self.nombre)   
    
class Productos(BaseModel):
    descripcion = models.CharField(max_length=300)
    referencia = models.CharField(unique=True, max_length=300)
    proveedor = models.ForeignKey(Proveedor,on_delete=models.PROTECT)
    costo_uni = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Producto"
        db_table = 'lista_productos'

    def __str__(self):
        return str(self.descripcion) + ' - ' + str(self.referencia)
    
    

    
    
    
    