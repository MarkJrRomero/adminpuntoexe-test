from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import CustomUser
from django.contrib.auth.models import Permission, ContentType
from django.utils.translation import gettext_lazy as _

admin.site.site_header = "Administración Punto exe."
admin.site.site_title = "Portal de Administracion"
admin.site.index_title = "Portal administración de Punto exe."

class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'codename')

class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (_('Credenciales'), {'fields': ('username', 'password')}),
        (_('Información Personal'), {'fields': ('email', 'first_name', 'cedula', 'telefono')}),
        (_('Administración'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Grupos y Permisos'), {'fields': ('groups', 'user_permissions')}),
        (_('Datos Importantes'), {'fields': ('last_login', 'date_joined')}),
    )
    
    list_display = ('id', 'username', 'email', 'first_name', 'cedula', 'is_staff')
    search_fields = ('username', 'cedula', 'email', 'first_name')
    ordering = ('id', 'username', 'cedula')

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Permission,PermissionAdmin)
admin.site.register(ContentType)