from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:    
        if request.method == 'POST':
            usuario = request.POST.get('usuario')
            password = request.POST.get('password')

            sesion = authenticate(request, username=usuario, password=password)

            if sesion is not None:
                if sesion.is_active:
                    login(request, sesion)
                    return redirect('dashboard')
                else:
                    messages.info(request, 'La cuenta no se encuentra activa. Verifique con su administrador')
            else: 
                messages.info(request, 'Usuario o Contraseña incorrectos')
        return render(request, "login.html", {})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')