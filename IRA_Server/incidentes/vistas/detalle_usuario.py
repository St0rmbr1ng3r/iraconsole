from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..modelos.usuario import Usuario
from ..modelos.formularios import FormularioModificarUsuario, FormularioDetalleUsuario
from django.contrib import messages

@login_required(login_url='login')
def cargar_usuario(request):
    if request.user.is_superuser:
        if request.method == 'GET':
            id_usuario=request.GET.get('id_usuario', '0')
            u = Usuario() 
            detalle = u.cargar_detalle_usuario(id_usuario)

            if detalle == 1:
                messages.error(request, "Usuario Invalido")
                return redirect('administracion')

            print(detalle[0][0])
            formulario = FormularioDetalleUsuario(initial={
                'id':int(detalle[0][0]), 
                'is_superuser': int(detalle[0][3]),
                'username' : detalle[0][4],
                'first_name' : detalle[0][5],
                'last_name' : detalle[0][6],
                'email' : detalle[0][7],
                'is_active' : int(detalle[0][8]),
                'date_joined' : detalle[0][10], 
                'last_login' : detalle[0][2]           
                })

            contexto = {'formulario':formulario} 
            return render(request, "detalle_usuario.html", contexto)

        #AGREGADO CON METODO POST
        if request.method == 'POST':
            formulario = FormularioModificarUsuario(request.POST)
            print("POST REQUEST")
            print(request.POST)
            print("CAMPO ID COULTO: ",request.POST['id_usuario'])

            print("FORMULARIO COMPLETO ENVIADO")
            print(formulario)

            if formulario.is_valid():
                print("Formulario Valido",formulario.cleaned_data)
                messages.success(request, "Usuario Actualizado Correctamente" )
                return redirect('administracion')
                '''
                ua = UsuarioModificado()
                if ua.actualizar_usuario(formulario.cleaned_data) == 1:
                    messages.error(request, "No se pueden guardar los cambios. Por favor intente nuevamente" )
                    return redirect('administracion')
                else:
                    messages.success(request, "Usuario Actualizdo Correctamente" )
                    return redirect('administracion')
                '''
            else:
                print("ERRORES DEL FORMULARIO")
                print (formulario.errors)
                messages.error(request, "No se pueden guardar los cambios. Por favor intente nuevamente" )
                return redirect('administracion')
        
    return redirect('dashboard')


@login_required(login_url='login')
def usuario_invalido(request):
    return render(request, "usuarioinvalido.html")