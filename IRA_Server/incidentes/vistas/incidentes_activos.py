from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..modelos.incidente import *
from django.template import Context

@login_required(login_url='login')
def cargar_incidentes_activos(request):
    incActivos = IncidentesActivos()
    contexto = {'inc_activos':incActivos.resIncActivos}
    return render(request, "incidentes_activos.html", contexto)