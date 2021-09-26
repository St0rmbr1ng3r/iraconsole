from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..modelos.usuario import Usuario

@login_required(login_url='login')
def cargar_admin(request):
    if request.user.is_superuser:
        ua = Usuario()
        usuarios = ua.listar_usuarios_activos()
        contexto = {'usuarios':usuarios}

        return render(request, "panel_administracion.html", contexto)

    return redirect('dashboard')
