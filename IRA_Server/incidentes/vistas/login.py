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
            print(request.user.username)

            sesion = authenticate(request, username=usuario, password=password)

            if sesion is not None:
                login(request, sesion)
                return redirect('dashboard')
            else: 
                messages.info(request, 'Usuario o Contraseña incorrectos')
        return render(request, "login.html", {})

def cerrar_sesion(request):
    logout(request)
    return redirect('login')