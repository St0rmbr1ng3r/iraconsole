from django.shortcuts import render, redirect
from ..modelos.incidente import NuevoIncidente #Incidentes, 
#from django.db import connection
#import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..modelos.formularios import FormularioMulti, FormularioIncidente

@login_required(login_url='login')
def crear_incidente(request):
    formulario = FormularioIncidente()
    formulariomulti = FormularioMulti()

    if request.method == 'POST':
        formulario = FormularioIncidente(request.POST)
        formulariomulti = FormularioMulti(request.POST)

        if formulario.is_valid():
            if formulariomulti.is_valid():
                ni = NuevoIncidente()
                if ni.guardar_incidente(formulario.cleaned_data, formulariomulti.cleaned_data) == 1:
                    messages.error(request, "Erro al guardar el incidente. Por favor intente nuevamente" )
                    return redirect('nuevo')
                else:
                    messages.success(request, "Incidente Creado Correctamente" )
                    return redirect('activos')
            else:
                print (formulariomulti.errors)
        else:
            print (formulario.errors)


    contexto = {'formulario':formulario, 'formulariomulti':formulariomulti}
    return render(request, "nuevoincidente.html", contexto)