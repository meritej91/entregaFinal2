from django.db import models


class Paciente(models.Model):
    def __str__(self):
        return f"Nombre: {self.nombre} --- Edad: {self.edad} --- Especie: {self.especie} --- Raza: {self.raza}"
    nombre = models.CharField(default=0, max_length=20)
    edad = models.IntegerField(default=0)
    especie = models.CharField(default=0, max_length=20)
    raza = models.CharField(default=0, max_length=20)

class Turno(models.Model):
    apellido = models.CharField(default=0, max_length=20)
    nombre = models.CharField(default=0, max_length=20)
    especie = models.CharField(default=0, max_length=20)
    dia = models.DateField(default=0, max_length=20)
    consulta = models.CharField(default=0, max_length=100)




