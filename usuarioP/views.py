__author__ = 'HICC2'
from django.template import RequestContext
from django.shortcuts import *
from asistenciaT.forms import LoginForm
from django.contrib.auth import authenticate,login

def login_page(request):
    name="Luis Liscano"
    message=None
    if request.method =="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    message="Login incorrecto"
                else:
                    message="usuario inactivo"
            else:
                message="nombre de usuario o password incorrectos "
    else:
        form=LoginForm()
    return render_to_response('login.html',{'message':message,'form':form,'name':name})