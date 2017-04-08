__author__ = 'HICC2'
#-*- coding: utf-8 -*-
from ckeditor.widgets import CKEditorWidget as ch

from django import forms
#importamos de django a Forms que se encarga de las directivas de los formulario
from .models import *
#luego importamos las clases de los modelos de la base de datos
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    Telefono=forms.IntegerField()

class RegistroF(forms.ModelForm):

    class Meta:
        model =Registro #le indicamos que tabla del modelo se va a trabajar
#fields = son  los campos que se van a usar
        fields=[
            'tecnico',
            'serial',
            'fecha' ,
            'historico',
            'estado',
        ]
#Label= El nombre que se va a sustituir
        labels={
            'tecnico':'Tecnico',
            'serial':'Serial HICC',
            'fecha':'Fecha',
            'historico':'Reseña historica',
            'estado':'ESTUS'
        }
#wiggets= son las configuraciones de cada tabla o campo al introducir
        widgets ={

            'tecnico':forms.Select(attrs={'class':'form-control control-label'}),
            'serial':forms.TextInput(attrs={'placeholder': 'Incerte serial', 'class':'form-control control-label'}),
            'fecha':forms.SelectDateWidget(attrs={'class':'btn-sm control-label'}),
            'historico':forms.TextInput(attrs={'class':'form-control control-label icon-bar'}),
            'estado':forms.Select(attrs={'class':'form-control control-label'}),
            }

        #help_texts={'serial':'se recomienda usar datos cuidadosamente ' }
        #'serial':forms.TextInput(attrs={'placeholder': 'Incerte serial', 'class':''}), el atributo (attrs ={aplicamos atributos a la etiqueta html})

class RepuestoF(forms.ModelForm):
    class Meta:
        model=Repuesto

        fields=[
            'tecnico',
            'serial',
            'pantalla',
            'lector',
            'memoria_ram',
            'fan_cooler',
            'computadora',
            'ele',]
        labels={
            'tecnico':'Tecnico',
            'serial':'Serial',
            'pantalla':'Pantalla',
            'lector':'Lector biometrico',
            'memoria_ram':'Memoria RAM',
            'fan_cooler':'Fan cooler',
            'computadora':'Computadora',
            'ele':'Panel frontal de alimentacion',
        }
        widgets={
            'tecnico':forms.Select,
            'serial':forms.TextInput,
            'pantalla':forms.CheckboxInput(attrs={'class':''}),
            'lector':forms.CheckboxInput(attrs={'class':''}),
            'memoria_ram':forms.CheckboxInput(attrs={'class':''}),
            'fan_cooler':forms.CheckboxInput(attrs={'class':''}),
            'computadora':forms.CheckboxInput(attrs={'class':''}),
            'ele':forms.CheckboxInput(attrs={'class':''}),
            }
