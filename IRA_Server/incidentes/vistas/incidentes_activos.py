from django.shortcuts import render #, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..modelos.incidente import *
#from django.template import Context
from django.contrib import messages

@login_required(login_url='login')
def cargar_incidentes_activos(request):
    ia = IncidentesActivos()
    incActivos = ia.listar_incidentes_activos
    contexto = {'inc_activos':incActivos}
    return render(request, "incidentes_activos.html", contexto)

