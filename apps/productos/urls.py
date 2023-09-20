from django.urls import path
from . import views, apps

app_name = 'productos'

urlpatterns = [
    
    path('menu_productos/', views.ProductosMenuView.as_view(), name='menu_productos'),
    
    #LISTA DE PRODUCTOS
    path('lista_productos/', views.VistaListadoProductos.as_view(), name='lista_productos'),
    path('data_productos/', views.DataListadoProductos.as_view(), name='data_productos'),
    
    #REGISTRO DE PRODUCTOS
    path('registrar_producto/', views.VistaRegistrarProductos.as_view(), name='registrar_producto'),
  
]