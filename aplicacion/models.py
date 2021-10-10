from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.urls import reverse
# Create your models here.
import datetime
from django.db import models






class Region(models.Model):
    NombreRegion = models.CharField(max_length=50)
    def __unicode__(self):
        return self.NombreRegion
    def __str__(self):
        return self.NombreRegion

class Departamento(models.Model):
    NombreDepartamento = models.CharField(max_length=50)
    Region = models.ForeignKey('Region',
    on_delete=models.CASCADE,)
    def __unicode__(self):
        return self.NombreDepartamento
    def __str__(self):
        return self.NombreDepartamento


class Municipio(models.Model):
    NombreMunicipo = models.CharField(max_length=50)
    Departamento = models.ForeignKey('Departamento',
    on_delete=models.CASCADE,)
    def __unicode__(self):
        return self.NombreMunicipo
    def __str__(self):
        return self.NombreMunicipo

class Comercio(models.Model):
    NombreComercio = models.CharField(max_length=50)
    Patente = models.CharField(max_length=50)
    Propietario = models.CharField(max_length=50)
    Municipio= models.ForeignKey('Municipio',
    on_delete=models.CASCADE,)
    def __unicode__(self):
        return self.NombreComercio
    def __str__(self):
        return self.NombreComercio

class Sucursal(models.Model):
    NombreSucursal = models.CharField(max_length=50)
    Comercio= models.ForeignKey('Comercio',
    on_delete=models.CASCADE,)
    Municipio= models.ForeignKey('Municipio',
    on_delete=models.CASCADE,)
    def __unicode__(self):
        return self.NombreSucursal
    def __str__(self):
        return self.NombreSucursal

class Queja(models.Model):
    DesQueja = models.CharField(max_length=500)
    created_at = models.DateTimeField(('Fecha creación'),
                                      default=timezone.now)
    Comercio= models.ForeignKey('Comercio',
    on_delete=models.CASCADE,)
    Sucursal= models.ForeignKey('Sucursal',
    on_delete=models.CASCADE,)
    def __unicode__(self):
        return self.DesQueja
    def __str__(self):
        return self.DesQueja
    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})
