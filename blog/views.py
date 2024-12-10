from django.shortcuts import render, get_object_or_404
from .formularios import ProfesoresForm, CursosForm, EstudiantesForm, EntregablesForm
from .models import Profesores, Cursos, Estudiantes, Entregables

def index(request):
    entregables = Entregables.objects.all()
    return render(request, 'index.html', {'Entregables': entregables})

def add_profesor(request):
    form = ProfesoresForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'add_profesor.html', {'form': form})

def add_curso(request):
    form = CursosForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'add_curso.html', {'form': form})

def add_estudiante(request):
    form = EstudiantesForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'add_estudiante.html', {'form': form})

def add_entregable(request):
    form = EntregablesForm
    if form.is_valid():
        form.save()
    return render(request, 'add_entregable.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    results = Entregables.objects.filter(titulo__icontains=query)
    return render(request, 'search_results.html', {'results': results})


# Create your views here.
