from django.contrib import admin

# Register your models here.
from django.contrib import admin

from aplicacion.models import *


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    pass

@admin.register(Comercio)
class ComercioAdmin(admin.ModelAdmin):
    pass


@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    pass

@admin.register(Queja)
class QuejasAdmin(admin.ModelAdmin):
    pass
