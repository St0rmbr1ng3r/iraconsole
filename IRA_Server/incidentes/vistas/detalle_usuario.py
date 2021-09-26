from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..modelos.usuario import Usuario

@login_required(login_url='login')
def cargar_usuario(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            id_usuario=request.GET.get('id_usuario', '0')
            da = Usuario()
            detalle = da.cargar_detalle_usuario(id_usuario)
            contexto = {'detalle':detalle}
            return render(request, "detalle_usuario.html", contexto)

    return redirect('dashboard')
