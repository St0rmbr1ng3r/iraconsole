from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..modelos.incidente import DetalleIncidente
from ..modelos.incidente import *
from django.contrib import messages


@login_required(login_url='login')
def cargar_incidente(request):
    if request.method == 'GET':
        id_inc=request.GET.get('id_inc', '0')
        di = DetalleIncidente()
        detalle = di.buscar_incidente(id_inc)
        if detalle == 1:
            return redirect('noencontrado')

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

        contexto = {'detalle':detalle, 'descripciones':descripciones}
        return render(request, "detalle_incidente.html", contexto)


@login_required(login_url='login')
def no_encontrado(request):
    return render(request, "sinresultado.html")