from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def cargar_incidente(request):

    if request.method == 'GET':
        print("REQUEST")
        print(request)
        id_inc=request.GET.get('id_inc', '0')
        print("ID INCIDENTE: ",id_inc)
        contexto = {}
        return render(request, "detalle_incidente.html", contexto)