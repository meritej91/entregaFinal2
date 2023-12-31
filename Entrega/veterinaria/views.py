from django.shortcuts import render
from django.http import HttpResponse 
from veterinaria.models import *
from veterinaria.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

def inicio(request):
    return render(request, "veterinaria/inicio.html")

def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get["username"]
            contra = form.cleaned_data.get["password"]

            user = authenticate(username=usuario,password=contra)

            if user :
                login(request, user)
                return render(request, "veterinaria/inicio.html", {"mensaje": f"Bienvenido {user}"})
            
        else:
            return render(request, "veterinaria/inicio.html", {"mensaje": "Datos incorrectos. Intentar nuevamente."})
    else:
        form = AuthenticationForm()

    return render(request, "veterinaria/logIn.html", {"formulario":form})



def registrar(request):
    
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "veterinaria/inicio.html", {"mensaje": "El usuario ha sido creado."})
        else:
            form = UserCreationForm()
    
    return render(request, "veterinaria/registrar.html", {"formulario":form})


def editarUsuario(request):

    usuario = request.user
    if request.method == "POST":
        form = formEditar(request.POST)
        if form.is_valid():
            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password = info["password1"]
            usuario.first_name = info["first_name"]
            usuario.second_name = info["second_name"]

            usuario.save()

            return render(request, "veterinaria/inicio.html")
    
    else:
        form = formEditar(initial ={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })

    return render(request, "veterinaria/inicio.html", {"formulario":form, "usuario":usuario})



def buscarPaciente(request):
    return render(request, "veterinaria/buscarPaciente.html")

def resultados(request):
    if request.GET["nombre"]:
        nombre= request.GET["nombre"]
        pacientes = Paciente.objects.filter(nombre__iexact = nombre)
        return render(request, "veterinaria/resultados.html", {"nombre":pacientes})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)


def formTurno(request):
    if request.method == "POST":

        form1 = formularioTurno(request.POST)
        
        if form1.is_valid():
            info = form1.cleaned_data
            turno = Turno(apellido=info["apellido"], nombre=info["nombre"], especie=info["especie"], dia=info["dia"], consulta=info["consulta"])
            turno.save()

            return render(request, "veterinaria/inicio.html")
        
    else:
        form1 = formularioTurno()

    return render(request, "veterinaria/formularioTurno.html", {"formulario1": form1})

def formPaciente(request):
    if request.method == "POST":

        form2 = formularioPaciente(request.POST)
        
        if form2.is_valid():
            info = form2.cleaned_data
            paciente = Paciente(nombre=info["nombre"], edad=info["edad"], especie=info["especie"], raza=info["raza"])
            paciente.save()

            return render(request, "veterinaria/inicio.html")
        
    else:
        form2 = formularioPaciente()

    return render(request, "veterinaria/nuevoPaciente.html", {"formulario2": form2})


def readPaciente(request):

    pacientes = Paciente.objects.all()
    contexto = {"mascotas":pacientes}
    return render(request, "veterinaria/leerPaciente.html", contexto)


def createPaciente(request):
    if request.method == "POST":

        form3 = formularioPaciente(request.POST)
        
        if form3.is_valid():
            info = form3.cleaned_data
            paciente = Paciente(nombre=info["nombre"], edad=info["edad"], especie=info["especie"], raza=info["raza"])
            paciente.save()

            return render(request, "veterinaria/inicio.html")
        
    else:
        form3 = formularioPaciente()

    return render(request, "veterinaria/crearPaciente.html", {"formulario2": form3})

def deletePaciente(request, pacienteNombre):

    paciente = Paciente.objects.get(nombre=pacienteNombre)
    paciente.delete()

    pacientes = Paciente.objects.all()
    contexto = {"mascotas":pacientes}
    return render(request, "veterinaria/leerPaciente.html", contexto)

def updatePaciente(request, pacienteNombre):
    paciente = Paciente.objects.get(nombre=pacienteNombre)
    if request.method == "POST":

        form4 = formularioPaciente(request.POST)
        
        if form4.is_valid():
            info = form4.cleaned_data
            paciente.nombre = info["nombre"]
            paciente.edad = info["edad"]
            paciente.especie = info["especie"]
            paciente.raza = info["raza"]

            paciente.save()

            return render(request, "veterinaria/inicio.html")
        
    else:
        form4 = formularioPaciente(initial={"nombre":paciente.nombre,"edad":paciente.edad, "especie":paciente.especie, "raza":paciente.raza})

    return render(request, "veterinaria/editarPaciente.html", {"formulario4": form4, "nombre":pacienteNombre})