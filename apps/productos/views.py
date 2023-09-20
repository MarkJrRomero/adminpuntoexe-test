from django.shortcuts import render #type: ignore
from django.shortcuts import render #type: ignore
from django.views.generic import TemplateView, View #type: ignore
from apps.productos.models import *
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
from .forms import *

# Create your views here.
class ProductosMenuView(MenuView, PermissionRequiredMixin, LoginRequiredMixin):
    permission_required = 'users.menu_productos'
    menu_options = [
        {
            'title': 'Listado de productos',
            'description': 'Modulo para ver los productos',
            'url': 'productos:lista_productos',
            'icon': 'flaticon2-soft-icons',
            'permission': 'users.listado_productos'
        },
        {
            'title': 'Registrar producto',
            'description': 'Modulo para registrar productos',
            'url': 'productos:registrar_producto',
            'icon': 'flaticon2-add',
            'permission': 'users.registrar_productos'
        },
    ]
    
    
    
class VistaListadoProductos(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = "users.listado_productos"
    template_name = 'productos/tabla_productos.html'

        
        
class DataListadoProductos(LoginRequiredMixin, PermissionRequiredMixin, ServerSideDatatableView):
    permission_required = "users.listado_productos"
    columns = [ 'id', 'descripcion' ,  'referencia' , 'proveedor__nombre' , 'costo_uni' ]
    
    def get_queryset(self):
        queryset = Productos.objects.filter(activo = True)
        if queryset.exists():
            return queryset
        else:
            return Productos.objects.none()        
        
class VistaRegistrarProductos(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = "users.registrar_productos"
    template_name = 'productos/registrar_producto.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductoForm
        return context
    
    def post(self, request, *args, **kwargs):
        
        try:
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({"success": True, "msj": "Se guardo el producto correctamente", "errors": str("")}, status=400)     
            else:   
                return JsonResponse({"success": False, "msj": "Hay errores en el formulario, por favor revise", "errors": str("")}, status=400)  
        except Exception as e:
            return JsonResponse({"success": False, "msj": str(e), "errors": str(e)}, status=400)