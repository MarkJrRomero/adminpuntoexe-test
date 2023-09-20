from django.shortcuts import render #type: ignore
from django.shortcuts import render #type: ignore
from django.views.generic import TemplateView, View #type: ignore
from apps.inventario.models import *
from apps.pages.views import MenuView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin #type: ignore
import random
from django.http import JsonResponse #type: ignore
from django_serverside_datatable.views import ServerSideDatatableView #type: ignore
from openpyxl import Workbook,load_workbook #type: ignore
from openpyxl.cell.cell import Cell #type: ignore
from openpyxl.styles import Alignment, Border, Font, NamedStyle, Side #type: ignore
from django.http import HttpResponse #type: ignore
from openpyxl.styles import PatternFill #type: ignore
from openpyxl.drawing.image import Image #type: ignore
from django.conf import settings #type: ignore
from pyrfc import Connection #type: ignore
from rest_framework.authentication import TokenAuthentication  #type: ignore
from rest_framework.permissions import IsAuthenticated  #type: ignore
from rest_framework.views import APIView  #type: ignore
from rest_framework.response import Response  #type: ignore
import datetime
import pytz #type: ignore
from django.db.transaction import atomic #type: ignore
# from .forms import *

# Create your views here.
class InventarioMenuView(MenuView, PermissionRequiredMixin, LoginRequiredMixin):
    permission_required = 'users.menu_productos'
    menu_options = [
        {
            'title': 'Inventario de productos',
            'description': 'Modulo para gestionar el inventario de productos',
            'url': 'inventario:vista_inventario',
            'icon': 'flaticon2-soft-icons',
            'permission': 'users.listado_productos'
        },
    ]
    
    
    
class VistaInventario(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = "users.listado_productos"
    template_name = 'inventario/vista_inventario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Productos.objects.filter(activo = True)
        return context   
        
        
class DataListadoInventario(LoginRequiredMixin, PermissionRequiredMixin, ServerSideDatatableView):
    permission_required = "users.listado_productos"
    columns = [ 'id', 'producto__descripcion', 'producto__referencia' ,  'cantidad' ]
    
    def get_queryset(self):
        queryset = Inventario.objects.filter(activo = True)
        if queryset.exists():
            return queryset
        else:
            return Inventario.objects.none()     
        
class ManejoInventario(LoginRequiredMixin, PermissionRequiredMixin, APIView):
    permission_required = "users.registrar_productos"
    
    def post(self, request, *args, **kwargs):
        
        try:
            producto = Productos.objects.filter(id=request.POST['producto']).first()
            cantidad = int(request.POST['cantidad'])
            tipo = str(request.POST['tipo'])
            
            inventarioActual = Inventario.objects.filter(producto=producto, activo = True).first()
            
            if not inventarioActual:

                if tipo == "resta":
                     return JsonResponse({"success": False, "msj": "No se puede restar el producto por que no cuenta con un inventario activo"}, status=400)
                
                Inventario.objects.create(
                    producto = producto,
                    cantidad = cantidad
                )
                return JsonResponse({"success": True, "msj": "Se registro el producto en el inventario con una cantidad inicial de: "+str(cantidad)}, status=200)
            else:
                
                if tipo == "suma":
                    
                    inventarioActual.cantidad = str(int(inventarioActual.cantidad) + cantidad)
                    inventarioActual.save()
                    return JsonResponse({"success": True, "msj": "Se le sumo al inventario del producto la nueva cantidad en stock es de: "+str(inventarioActual.cantidad)}, status=200)
                
                else:
                    
                    if inventarioActual.cantidad == 0:
                         return JsonResponse({"success": False, "msj": "No se puede restar al inventario por que actualmente es de 0"}, status=400)
                    
                    if cantidad > int(inventarioActual.cantidad):
                        return JsonResponse({"success": False, "msj": "No se puede restar al inventario por que la cantidad a restar es mayor a la cantidad actual"}, status=400)
                    
                    inventarioActual.cantidad =  str(int(inventarioActual.cantidad) - cantidad)
                    inventarioActual.save() 
                    return JsonResponse({"success": True, "msj": "Se le resto al inventario del producto el stock actual es de: "+str(inventarioActual.cantidad)}, status=200)
                    
                
                
            
            # if form.is_valid():
            #     form.save()
            #     return JsonResponse({"success": True, "msj": "Se guardo el producto correctamente", "errors": str("")}, status=400)     
            # else:   
            #     return JsonResponse({"success": False, "msj": "Hay errores en el formulario, por favor revise", "errors": str("")}, status=400)  
        except Exception as e:
            return JsonResponse({"success": False, "msj": str(e), "errors": str(e)}, status=400)