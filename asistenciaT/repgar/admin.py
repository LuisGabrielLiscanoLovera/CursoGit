from django.contrib import admin
from .models import *
from .form import *

# Register your models here.
admin.site.register(Perfiles)
admin.site.register(DatosTecnico)
admin.site.register(Registro)
admin.site.register(Repuesto)

