from django.contrib import admin
from Cajas.models import Cajas,Empleados, Sucursales, TipoEmpleado

# Register your models here.

class CajasAdmin(admin.ModelAdmin):pass
class EmpleadosAdmin(admin.ModelAdmin):pass
class SucursalesAdmin(admin.ModelAdmin):pass
class TipoEmpleadoAdmin(admin.ModelAdmin):pass

admin.site.register(Cajas,CajasAdmin)
admin.site.register(Empleados,EmpleadosAdmin)
admin.site.register(Sucursales,SucursalesAdmin)
admin.site.register(TipoEmpleado,TipoEmpleadoAdmin)


