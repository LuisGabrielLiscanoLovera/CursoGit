# -*- coding: utf-8 -*-
__author__ = 'Luis Gabriel Liscano Lovera (ccidbcomputacion12@gmail.com)'
# Create your views here.
from django.shortcuts import *
from .form import *
from .models import *
from django.db.models import *
from  django.views.generic import ListView #listar
from django.views.generic.detail import DetailView #detallado
from django.views.generic.edit import CreateView, UpdateView,DeleteView # vista mejorada
from  django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,FormView
from django import forms
from datetime import datetime as dt


def holapdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
 
    temp = StringIO()
 
    # Create the PDF object, using the StringIO object as its "file."
    p = canvas.Canvas(temp)
 
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
 
    # Close the PDF object cleanly.
    p.showPage()
    p.save()
 
    # Get the value of the StringIO buffer and write it to the response.
    response.write(temp.getvalue())
    return response




def Home(request):
    name="Luis Liscano"
    tiempo=dt.now()
    if (tiempo.hour >= 12):
        hora=(str(tiempo.hour-12)+":"+str(tiempo.minute)+(': PM'))
    else:
        hora=(str(tiempo.hour)+":"+str(tiempo.minute)+(': AM'))


    return render_to_response('base/index.html',locals())





def repuesto(request):
    R=Repuesto.objects.all()
    name="Repuesto"
    return render_to_response('repuesto/repuesto.html',locals())


def FormRegistro(request):
    if request.method == 'POST':
        form = RegistroF(request.POST)
        if form.is_valid():
            form.save()
        return redirect('registro')
    else:
        form = RegistroF()
    return render(request, 'registro/form_registro.html', {'form':form},locals())


def FR(request):
    if request.method == 'POST':
        form=RepuestoF(request.POST)
        if form.is_valid():
            form.save()
        else:
            html='<html><head><title>ERROR</title></head><body style="background-color:#8aa4be" ><center><h1>Error al cargar el registro </h1><br><p >Es posible que los datos que intenta rigistrar pueden estar erroneo o puede que el <em>(Serial)</em> se encuentra duplicado</p><br><a href="{% url "d" %}">back</a></a></center></body></html>'
            return HttpResponse(html)
        return redirect('repuesto')

    else:
        form=RepuestoF()
    return render(request,'repuesto/form_Repuesto.html',{'form':form})

def registro(request):
    rg=Registro.objects.all().order_by('serial')
    name="Registro"
    #search=Registro.objects.filter(serial='')
    return render_to_response('registro/registro.html',locals())


def Buscar(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        busqueda=Registro.objects.filter(serial__icontains=q)
        return render(request,'registro/buscar.html', locals())
    else:
        return HttpResponse ('<body style="background-color:#8aa4be" ><center><h1>Busqueda Fallida</h1><br><p >Es posible que los datos que intenta Buscar pueden estar erroneo o <em>(Serial)</em> Invalidao</p><br><a href="/registro/ %}">Regresar</a></a></center></body></html>')

def eliminar_registro(request):
    eliminar = Registro.objects.all()
    eliminar.delete()
    return render_to_response('registro/registro.html')




def contacto(request):
    if request.method=='POST':#si el formulario es enviado
        form= Formulario(request.POST)
        if form.is_valid():#Si el formulario es valido se prosesan los datos
            return HttpResponseRedirect('gracias/')

    else:
        form=Formulario()
    return render_to_response('registro/registroUser.html',{'form':form})

def gracias(request):
    html='<!DOCTYPE html><html><head><title>Gracias SSAS</title></head><body><center><div class="container"><div class="row"><div class="col-md-12 well bg-info"><h1>Gracias por enviarnos su comentarios XD</h1></div></div></div></center></body></html>'
    return HttpResponse(html)


#Vista basadas en Clases import :(from  django.views.generic import ListView)
class vbc(ListView):
    model = Registro
    template_name = ('registro/registrovbc.html')
    #context_object_name = 'listar')
    #listar fino
'''
El parametro (context_object_name = 'newname') cambiamos el nombre del atributo para el recorrido de la lista
en la pantilla ejm en vez de der {% for Registro in object_list %} podemos cambiarlo por:
{% for Registro in newname %}

'''
class create(CreateView):
    model = Registro
    form_class = RegistroF
    template_name = ('registro/tarea_form.html')
    success_url = reverse_lazy('repuesto')

    #fields = ['serial','fecha','historico','tecnico']
    '''Comente el fields ya que se dispone un de una class de formulario( forms.py) personalizado y cargado con el parametro form_class'''
    #crear un objeto en la bd fino




'''
class detalle(DetailView):
    model = Registro
    template_name = ('registro/tarea_detail.html')
    #context_object_name ='postdetail'
    slug_field = 'serial'
    def get_queryset(self):
        query= super(detalle,self).get_queryset()
        return query.filter(serial=True)
'''



class Registrarse(FormView):
    template_name = ('registro/registrarse.html')
    form_class = UserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user =form.save()
        perfil=Perfiles()
        perfil.usuario=user
        perfil.telefono = form.cleaned_data['telefono']
        perfil.save()
        return super(Registrarse,self).form_valid(form)


class editar(UpdateView):
    model = Registro
    form_class = RegistroF
    #template_name = ('registro/registrovbc.html')
    template_name = ('registro/tarea_form.html')
    success_url = reverse_lazy('repuesto')
    #fields = ['serial','fecha','historico','tecnico']





class eliminar(DeleteView):
    model = Registro
    template_name = ('registro/eliminar.html')
    success_url = reverse_lazy('home')

#************************vista basada en clase (TemplateView)
class practicaHTML(TemplateView):
    template_name = ('practicaHTML/practica.html')
