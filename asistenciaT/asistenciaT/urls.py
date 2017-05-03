__author__ = 'Luis Gabriel Liscano Lovera (ccidbcomputacion12@gmail.com)'
"""asistenciaT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from repgar.views import *
#from asistenciaT.views import *
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required #con esta funcion permite restringir al usuario entrar al logearce
from django.conf.urls import url, include

from django.urls import resolve

urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^home/',login_required(Home), name='home'),

#****************************url en control de usuarios*********************************************
    url(r'^$',login,{'template_name':'login.html'},name='login'),
    url(r'^logout/',logout,{'template_name':'logout.html'},name='logout'),
    url(r'^registrarse/',Registrarse.as_view(), name='Registrarse'),

#****************************url en vistas bsadas en clases*****************************************
    url(r'^vbc/',login_required(vbc.as_view()), name='vbc'),#listar fino
    url(r'^create/',login_required(create.as_view()), name='new'),#create fino

#*************************Practica HTML************************************************************
    url(r'^html/',login_required(practicaHTML.as_view()), name='html'),#create fino


#************************************aplicar detail*************************************************
    #url(r'^(?P<pk>\d+)$',login_required(detail.as_view()), name='detail'),
    #url(r'^post/(?P<pk>\d+)/', login_required(detail.as_view()), name='detail'),
    #url(r'^detalles/',login_required(detail.as_view()), name='detail'),
    #url(r'^(?P<slug>[-_\w]+)/$',detalle.as_view(),name='post-detail'),

#****************************************************************************************************
    url(r'^editar/(?P<pk>\d+)/$',login_required(editar.as_view()), name='editar'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(editar.as_view()), name='editar'),
    url(r'^borrar/(?P<pk>\d+)/$',login_required(eliminar.as_view()), name='delete'),
#****************************************************************************************************


    url(r'^eliminar/',login_required(eliminar_registro), name='eliminar'),



    url(r'^buscar/',login_required(Buscar), name='buscar'),




    url(r'^repuesto/',login_required(repuesto), name='repuesto'),
    url(r'^registro/',login_required(registro), name='registro'),
    url(r'^registrohicc/',login_required(FormRegistro), name='FDR'),
    url(r'^repuestohicc/',login_required(FR), name='FRP'),
    #url(r'^prueba/',login_required(consulta), name='consulta'),
    url(r'^contacto/',login_required(contacto), name='contacto'),
    url(r'^gracias/',login_required(gracias), name='gracias'),

    #url(r'^pdf/',pdf, name='pdf'),

    #url(r'^login/',login_page),
    #url(r'^login/',login,{'template_name':'base/index.html'},name='login'),


    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
