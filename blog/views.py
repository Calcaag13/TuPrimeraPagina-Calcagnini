from django.shortcuts import render, redirect
from .formularios import EstudiantesForm, ProfesoresForm, CursosForm, EntregablesForm, SearchForm  
from .models import Profesores, Cursos, Estudiantes, Entregables

def home(request):
    return render(request, 'blog/index.html')

def add_curso(request):
    if request.method == 'POST':
        form = CursosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = CursosForm()
    return render(request, 'blog/add_curso.html', {'form': form})


def add_entregable(request):
    if request.method == 'POST':
        form = EntregablesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = EntregablesForm()
    return render(request, 'blog/add_entregable.html', {'form': form})


def add_estudiante(request):
    if request.method == 'POST':
        form = EstudiantesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = EstudiantesForm()
    return render(request, 'blog/add_estudiante.html', {'form': form})


def add_profesor(request):
    if request.method == 'POST':
        form = ProfesoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:home')
    else:
        form = ProfesoresForm()
    return render(request, 'blog/add_profesor.html', {'form': form})

def search(request):
    results = []
    if request.method == 'GET' and 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            
            estudiantes = Estudiantes.objects.filter(nombre_estudiante__icontains=query)
            profesores = Profesores.objects.filter(nombre_profe__icontains=query)
            cursos = Cursos.objects.filter(curso__icontains=query)
            entregables = Entregables.objects.filter(nombre_entrega__icontains=query)

            results = list(estudiantes) + list(profesores) + list(cursos) + list(entregables)
    else:
        form = SearchForm()

    return render(request, 'blog/search_results.html', {'form': form, 'results': results})
