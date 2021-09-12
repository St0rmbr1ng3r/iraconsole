from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..modelos.incidente import DetalleIncidente

@login_required(login_url='login')
def cargar_incidente(request):

    if request.method == 'GET':
        id_inc=request.GET.get('id_inc', '0')
        di = DetalleIncidente()
        detalle = di.buscar_incidente(id_inc)

        descripciones = []

        if detalle[0][6] == 1:
            print("No hubo Clientes Afectados")
            descripciones.append("No hubo Clientes Afectados")
        else:
            print("Hay Clientes Afectados")
            descripciones.append("Hay Clientes Afectados")

        if detalle[0][7] == 1:
            print("No hubo Proveedores Involucrados")
            descripciones.append("No hubo Proveedores Involucrados")
        else:
            print("Hay Proveedores Involucrados")
            descripciones.append("Hay Proveedores Involucrados")

        if detalle[0][8] == 1:
            print("Activos Afectados 0-25%")
            descripciones.append("Activos Afectados 0-25%")
        else:
            print("Mayor a 25%")
            descripciones.append("Mayor a 25%")
    
        contexto = {'detalle':detalle}
        return render(request, "detalle_incidente.html", contexto)