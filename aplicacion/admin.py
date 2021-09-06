from django.contrib import admin

# Register your models here.
from django.contrib import admin

from aplicacion.models import *

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    pass

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass

@admin.register(Enfermedad)
class EnfermedadAdmin(admin.ModelAdmin):
    pass

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    pass