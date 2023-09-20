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
class PedidosMenuView(MenuView, PermissionRequiredMixin, LoginRequiredMixin):
    permission_required = 'users.menu_productos'
    menu_options = [
        {
            'title': 'Listado de pedidos',
            'description': 'Modulo para ver el listado de pedidos',
            'url': 'pedidos:menu_pedidos',
            'icon': 'flaticon2-soft-icons',
            'permission': 'users.listado_productos'
        },
        {
            'title': 'Crear un pedido',
            'description': 'Modulo para registrar productos',
            'url': 'pedidos:registrar_pedido',
            'icon': 'flaticon-add',
            'permission': 'users.registrar_pedido'
        },
    ]
    
    
class VistaRegistrarPedidos(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    permission_required = "users.registrar_pedido"
    template_name = 'pedidos/registrar_pedido.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PedidoForm
        context['productos'] = Productos.objects.filter(activo = True)
        return context
    
    # def post(self, request, *args, **kwargs):
        
    #     try:
    #         form = ProductoForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return JsonResponse({"success": True, "msj": "Se guardo el producto correctamente", "errors": str("")}, status=400)     
    #         else:   
    #             return JsonResponse({"success": False, "msj": "Hay errores en el formulario, por favor revise", "errors": str("")}, status=400)  
    #     except Exception as e:
    #         return JsonResponse({"success": False, "msj": str(e), "errors": str(e)}, status=400)