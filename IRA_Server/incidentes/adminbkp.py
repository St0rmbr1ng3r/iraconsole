from django.contrib import admin

from .models import *

#REGISTRO DE MODELOS
admin.site.register(activo)
admin.site.register(ambiente)
admin.site.register(comentario)
admin.site.register(criticidadservicio)
admin.site.register(documento)
admin.site.register(estado)
admin.site.register(etapa)
admin.site.register(impacto)
admin.site.register(origen)
admin.site.register(servicio)
admin.site.register(severidad)
admin.site.register(tipoincidente)
admin.site.register(ubicacion)
admin.site.register(urgencia)