from django.shortcuts import render, redirect
from ..modelos.incidente import Incidentes, NuevoIncidente
from django.db import connection
from ..form import FormNuevoIncidente
import datetime
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
                    return redirect('nuevo')
                else:
                    return redirect('dashboard')
            else:
                print (formulariomulti.errors)
        else:
            print (formulario.errors)


    contexto = {'formulario':formulario, 'formulariomulti':formulariomulti}
    return render(request, "nuevoincidente.html", contexto)
