from django import forms
from .models import Profesores, Cursos, Estudiantes, Entregables

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model = Profesores
        fields = ['nombre_profe', 'apellido_profe','email_profe','profesion']

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ['curso','camada']

class EstudiantesForm(forms.ModelForm):
    class Meta:
        model = Estudiantes
        fields = ['nombre_estudiante','apellido_estudiante','email_estudiante']

class EntregablesForm(forms.ModelForm):
    class Meta:
        model = Entregables
        fields = ['nombre_entrega','fecha_de_entrega','entregado']


