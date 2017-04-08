__author__ = 'Luis Gabriel Liscano Lovera (ccidbcomputacion12@gmail.com)'
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.

class DatosTecnico(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    cedula=models.CharField(max_length=8,primary_key=True)
    SEXO = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('O', 'Otro'),
    )
    sexo = models.CharField(max_length=1, choices=SEXO)
    Telefono=models.CharField(max_length=11)
    correo_corporativo=models.EmailField(null=True, blank=True)
    def __str__(self):
        return self.nombres

class Registro(models.Model):
    tecnico=models.ForeignKey(DatosTecnico, null=True, blank=False, on_delete=models.CASCADE)
    serial=models.CharField(max_length=16)
    fecha =models.DateField()
    historico=RichTextField()
    ESTADO = (
        ('R','REPARADO'),
        ('C','CAMBIO'),
    )
    estado=models.CharField(max_length=1, choices=ESTADO)
    #historico=models.TextField()
    def __str__(self):
        return self.serial

class Repuesto(models.Model):
    tecnico=models.ForeignKey(DatosTecnico, null=True, blank=False, on_delete=models.CASCADE)
    serial=models.CharField(max_length=16, primary_key=True, )
    pantalla=models.BooleanField()
    lector=models.BooleanField()
    memoria_ram=models.BooleanField()
    fan_cooler=models.BooleanField("ventilador")
    computadora=models.BooleanField()
    ele=models.BooleanField("Soket de alimentacion" )
    def __str__(self):
        return self.serial


class Perfiles(models.Model):
    usuario=models.OneToOneField(User)
    telefono=models.CharField(max_length=11)
    def __str__(self):
        return self.usuario.username





