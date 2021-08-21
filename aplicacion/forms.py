from django.forms import ModelForm
from .models import Empleado, Cargo, TipoContratacion
class EmpleadoForm(ModelForm):
    class Meta:
         model = Empleado
         exclude = ['fecha', 'id_biometrico'] 