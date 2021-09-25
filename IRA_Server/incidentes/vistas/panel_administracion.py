from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(lambda u: u.is_superuser)
def cargar_admin(request):
    return render(request, "panel_administracion.html")
