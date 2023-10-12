from django.urls import path
from veterinaria.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("logIn/", logIn, name="logIn"),
    path("formularioTurno/", formTurno, name="turno"),
    path("registrar/", registrar, name="registro"),
    path("logOut", LogoutView.as_view(template_name="veterinaira/logOut.html"), name="cerrarSesion"),
    path("editar/", editarUsuario, name="editarUsuario"),
    path("buscarPaciente/", buscarPaciente, name="buscar"),
    path("resultados/", resultados, name="resultados"),
    path("nuevoPaciente/", formPaciente, name="nuevoPaciente"),

    #CRUD
    path("leerPaciente/", readPaciente, name="readPaciente"),
    path("crearPaciente/", createPaciente, name="createPaciente"),
    path("eliminarPaciente/<pacienteNombre>/", deletePaciente, name="deletePaciente"),
    path("editarPaciente/<pacienteNombre>/", updatePaciente, name="updatePaciente"),
]
