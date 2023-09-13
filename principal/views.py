from msilib.schema import ListView
from django.contrib import messages  
from django.shortcuts import render, redirect
from principal.models import *
from .models import Usuarios
# from django.http import HttpResponse

def home(request):
    usuariosListado = Usuarios.objects.all()
    messages.success(request, '¡Listado!')
    return render(request, "index.html", {"usuarios": usuariosListado})

def registrarUsuario(request):
    username = request.POST['textUsername']
    content = request.POST['textEmail']
    password = request.POST['textPassword']

    usuario = Usuarios.objects.create(username=username, content=content, password=password)
    messages.success(request, 'Usuario Registrado!')
    return redirect('/')

def edicionUsuario(request, usuario):
    usuario = Usuarios.objects.get(usuario=usuario)
    return render(request, "edicionUsuario.html", {"curso": usuario})


def editarUsuario(request, usuario_id):
    # Obtén el objeto Usuarios utilizando el usuario_id
    usuario = Usuarios.objects.get(id=usuario_id)

    if request.method == 'POST':
        # Procesa los datos del formulario de edición y actualiza el usuario
        username = request.POST['textUsername']
        email = request.POST['textEmail']
        password = request.POST['textPassword']

        usuario.username = username
        usuario.email = email
        usuario.password = password
        usuario.save()
        messages.success(request, 'Usuario Actualizado!')

        return redirect('/')

    # Renderiza el formulario de edición con los datos del usuario
    return render(request, "edicionUsuarios.html", {"usuario": usuario})


def eliminarUsuario(request, id):
    usuarios = Usuarios.objects.get(id=id)
    usuarios.delete()

    messages.success(request, 'Usuario eliminado!')


    return redirect('/')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Tema\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def HomeT(request):
    temas = Temas.objects.all()  
    return render(request, "index1.html", {'temas': temas})

def registrarTema(request):
    title = request.POST['textTittlo']
    content = request.POST['textContenido']
    fecha = request.POST['textFecha']

    tema = Temas.objects.create(title=title, content=content, fecha=fecha)
    messages.success(request, 'Tema Registrado!')
    return redirect('/')
