
from io import UnsupportedOperation
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def cargar_admin(request):
    if request.user.is_superuser:
        usuarios = ["username","correo@correo.com","22-09-2021 12:25:25","24-09-2021 16:35:15"]
        contexto = {'usuarios':usuarios}
        return render(request, "panel_administracion.html", contexto)

    return redirect('dashboard')
