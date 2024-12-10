from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_profesor/', views.add_profesor, name='add_profesor'),
    path('add_curso/', views.add_curso, name='add_curso'),
    path('add_estudiante/', views.add_estudiante, name='add_estudiante'),
    path('add_entregable/', views.add_entregable, name='add_entregable'),
    path('search/', views.search, name='search'),
]
