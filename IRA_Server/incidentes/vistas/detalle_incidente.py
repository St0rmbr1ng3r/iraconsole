from django.shortcuts import render#, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
<<<<<<< HEAD
from ..modelos.incidente import DetalleIncidente
=======
from modelos.incidente import *
>>>>>>> 8ca3a83 (Busqueda de Incidnetes y Detalle)
=======
from ..modelos.incidente import *
>>>>>>> 3e031a8 (modulo no importado)

@login_required(login_url='login')
def cargar_incidente(request):

<<<<<<< HEAD
    if request.method == 'GET':
=======
     if request.method == 'GET':
>>>>>>> 8ca3a83 (Busqueda de Incidnetes y Detalle)
        id_inc=request.GET.get('id_inc', '0')
        di = DetalleIncidente()
        detalle = di.buscar_incidente(id_inc)
        multiples = di.buscar_detalle_incidente(id_inc)

        descripciones = []

        if detalle[0][6] == 1:
            descripciones.append("No hubo Clientes Afectados")
        else:
            descripciones.append("Hay Clientes Afectados")

        if detalle[0][7] == 1:
            descripciones.append("No hubo Proveedores Involucrados")
        else:
            descripciones.append("Hay Proveedores Involucrados")

        if detalle[0][8] == 1:
            descripciones.append("Activos Afectados 0-25%")
        else:
            descripciones.append("Mayor a 25%")

        print(multiples)

        contexto = {'detalle':detalle, 'descripciones':descripciones}
        return render(request, "detalle_incidente.html", contexto)