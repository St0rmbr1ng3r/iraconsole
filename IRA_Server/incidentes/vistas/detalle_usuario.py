from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..modelos.usuario import Usuario
from ..modelos.formularios import FormularioModificarUsuario

@login_required(login_url='login')
def cargar_usuario(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            id_usuario=request.GET.get('id_usuario', '0')
            da = FormularioModificarUsuario()
            detalle = da.cargar_detalle_usuario(id_usuario)

            print(type(detalle))

            if detalle == 1:
                return redirect('usuarioinvalido')
            
            usuario = Usuario()

            usuario.id = int(detalle[0][0])
            usuario.password = detalle[0][1]
            usuario.last_login = detalle[0][2]
            usuario.is_superuser = int(detalle[0][3])
            usuario.username = detalle[0][4]
            usuario.first_name = detalle[0][5]
            usuario.last_name = detalle[0][6]
            usuario.email = detalle[0][7]
            usuario.is_active = int(detalle[0][8])
            usuario.date_joined = detalle[0][10]

            contexto = {'usuario':usuario}
            return render(request, "detalle_usuario.html", contexto)

    return redirect('dashboard')


@login_required(login_url='login')
def usuario_invalido(request):
    return render(request, "usuarioinvalido.html")