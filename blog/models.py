from django.db import models

# Create your models here.

class Profesores(models.Model):
    nombre_profe = models.CharField(max_length=100)
    apellido_profe = models.CharField(max_length=100)
    email_profe = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cursos(models.Model):
    curso = models.CharField(max_length=100)
    camada = models.CharField(max_length=100)

    def __str__(self):
        return self.curso

class Estudiantes(models.Model):
    nombre_estudiante = models.CharField(max_length=100)
    apellido_estudiante = models.CharField(max_length=100)
    email_estudiante = models.EmailField()

    def __str__(self):
        return self.nombre
    
class Entregables(models.Model):
    nombre_entrega = models.CharField(max_length=100)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField(default=True)
