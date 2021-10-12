from django.shortcuts import render, redirect
from ..modelos.usuario import NuevoUsuario 
from django.contrib.auth.decorators import login_required
from ..modelos.formularios import FormularioUsuario

@login_required(login_url='login')
def crear_usuario(request):
    formulario = FormularioUsuario()

    if request.method == 'POST':
        formulario = FormularioUsuario(request.POST)

        if formulario.is_valid():
                nu = NuevoUsuario()
                if nu.guardar_usuario(formulario.cleaned_data) == 1:
                    return redirect('nuevousuario')
                else:
                    return redirect('administracion')
        else:
            print (formulario.errors)
        
        
    contexto = {'formulario':formulario}

    return render(request, "nuevousuario.html", contexto)