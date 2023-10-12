from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class formularioTurno(forms.Form):
    apellido = forms.CharField()
    nombre = forms.CharField()
    especie = forms.CharField()
    dia = forms.DateField()
    consulta = forms.CharField()

class formularioPaciente(forms.Form):
    nombre = forms.CharField()
    especie = forms.CharField()
    raza = forms.CharField()
    edad = forms.IntegerField()

class UsuarioNuevo(UserCreationForm):
    apellido = forms.CharField()
    nombre = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class formEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]