'''__author__ = 'loguin'
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import *
def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm[request.POST]
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario =UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

'''