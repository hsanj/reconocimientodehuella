from django.db import models

# Create your models here.
import datetime
from django.db import models


class Cargo(models.Model):
    nombre_cargo = models.CharField(max_length=40)
    def __unicode__(self):
        return self.nombre_cargo
    def __str__(self):
        return self.nombre_cargo

class TipoContratacion(models.Model):
    nombre_contratacion = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre_contratacion
    def __str__(self):
        return self.nombre_contratacion

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    id_biometrico = models.IntegerField()
    
    nit = models.CharField(max_length=17)
    
    telefono = models.CharField(max_length=10)
    
    cargo = models.ForeignKey('Cargo',
    on_delete=models.CASCADE,)
    tipo_contratacion = models.ForeignKey('TipoContratacion',
    on_delete=models.CASCADE,)

    def __unicode__(self):
        return "%s - %s" % ( self.nombre, self.dui )
    def __str__(self):
        return self.nombre


class TiemposAccesso(models.Model):
 entrada = models.DateTimeField(auto_now_add=True)
 salidad = models.DateTimeField(auto_now_add=True)
 is_open = models.IntegerField(default='1')
 empleado = models.ForeignKey('Empleado',
    on_delete=models.CASCADE,)
 def save(self, *args, **kwargs):
    if self.id:
        self.salidad = datetime.datetime.today()
        return super(TiemposAccesso, self).save(*args, **kwargs)