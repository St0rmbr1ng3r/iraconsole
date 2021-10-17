from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..modelos.usuario import *
from django.contrib import messages #import messages


@login_required(login_url='login')
def eliminar_usuario(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            id_usuario = request.GET.get('id_usuario', '0')
            u = Usuario()
            eliminacion = u.eliminar_usuario(id_usuario)
            if eliminacion == 0:
                messages.success(request, "Usuario Eliminado Correctamente" )
                return redirect('administracion')
            else:
                messages.error(request, "No se Pudo eliminar el Usuario Seleccionado")
        else:
            print("VA POR POST")
    messages.error(request, "No Tiene permisos para ver el recurso")
    return redirect('dashboard')
