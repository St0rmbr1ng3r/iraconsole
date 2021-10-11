from django.shortcuts import render#, redirect
#from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..modelos.dashboard import DashboardSeveridades, DashboardTop
#from django.template import Context
<<<<<<< HEAD

=======
>>>>>>> 345c36aa0fc6c31cfc25f6011884933cc60a6bf2

@login_required(login_url='login')
def cargar_dashboard(request):

    severidades = DashboardSeveridades()
    topValores = DashboardTop()

    print(topValores.contServicio)

    contexto = {'severidad':severidades,'servicio':topValores.contServicio,'ubicacion':topValores.contUbicacion,
    'ambiente':topValores.contAmbiente,'tipo':topValores.contTipo,'origen':topValores.contOrigen}
    return render(request, "dashboard.html", contexto)
