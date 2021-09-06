from django.db import models

# Create your models here.
import datetime
from django.db import models


class Doctor(models.Model):
    NombreDoc = models.CharField(max_length=50)
    DireccionDoc = models.CharField(max_length=50)
    TelefonoDoc = models.CharField(max_length=15)

    def __unicode__(self):
        return self.NombreDoc
    def __str__(self):
        return self.NombreDoc

class Enfermedad(models.Model):
    NombreEnfermedad= models.CharField(max_length=50)
    def __unicode__(self):
        return self.NombreEnfermedad
    def __str__(self):
        return self.NombreEnfermedad

class Medicamento(models.Model):
    NombreMedicamento= models.CharField(max_length=50)
    def __unicode__(self):
        return self.NombreMedicamento
    def __str__(self):
        return self.NombreMedicamento

class Paciente(models.Model):
    NombrePaciente = models.CharField(max_length=50)
    Doctor = models.ForeignKey('Doctor',
    on_delete=models.CASCADE,)
    Enfermedad = models.ForeignKey('Enfermedad',
    on_delete=models.CASCADE,)
    Medicamento = models.ForeignKey('Medicamento',
    on_delete=models.CASCADE,)

    def __unicode__(self):
        return self.NombrePaciente
    def __str__(self):
        return self.NombrePaciente