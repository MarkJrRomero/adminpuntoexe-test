from django.urls import path
from . import views, apps

app_name = 'inventario'

urlpatterns = [
    
    path('menu_inventario/', views.InventarioMenuView.as_view(), name='menu_inventario'),
    
    # #LISTA DE PRODUCTOS
    path('vista_inventario/', views.VistaInventario.as_view(), name='vista_inventario'),
    path('data_inventario/', views.DataListadoInventario.as_view(), name='data_inventario'),
    
    # #REGISTRO DE PRODUCTOS
    path('manejo_inventario/', views.ManejoInventario.as_view(), name='manejo_inventario'),
  
]