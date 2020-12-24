from django.contrib import admin

# Register your models here.

from myapp.models import Cancion
from myapp.models import Estilo
from myapp.models import Interprete

# Consultar las redes (no hay ninguna todavía).

admin.site.register(Cancion)
admin.site.register(Estilo)
admin.site.register(Interprete)
