from django.contrib import admin

# Register your models here.
from django.contrib import admin

from aplicacion.models import *

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoContratacion)
class TipoContratacionAdmin(admin.ModelAdmin):
    pass

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    pass

@admin.register(TiemposAccesso)
class TiemposAccessoAdmin(admin.ModelAdmin):
    pass