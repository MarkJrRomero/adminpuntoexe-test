from django.urls import path
from . import views, apps

app_name = 'pedidos'

urlpatterns = [
    
    path('menu_pedidos/', views.PedidosMenuView.as_view(), name='menu_pedidos'),
    
    # #LISTA DE PRODUCTOS
    # path('lista_productos/', views.VistaListadoProductos.as_view(), name='lista_productos'),
    # path('data_productos/', views.DataListadoProductos.as_view(), name='data_productos'),
    
    # #REGISTRO DE PRODUCTOS
    path('registrar_pedido/', views.VistaRegistrarPedidos.as_view(), name='registrar_pedido'),
  
]