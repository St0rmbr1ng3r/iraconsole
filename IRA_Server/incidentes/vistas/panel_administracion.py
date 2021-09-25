
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def cargar_admin(request):
    if request.user.is_superuser:
        return render(request, "panel_administracion.html")

    return render(request, "dashboard.html")
