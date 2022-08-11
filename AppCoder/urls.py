"""ProyectoCoder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppCoder import views
from AppCoder.views import curso, curso_formulario, profesor_formulario, busqueda_generacion, estudiante_formulario, buscar

urlpatterns = [
    path('inicio', views.inicio, name = 'Inicio'),
    path('cursos', views.curso, name = 'Cursos'),
    path('profesores', views.profesores, name = 'Profesores'),
    path('estudiantes', views.estudiantes, name = 'Estudiantes'),
    path('entregables', views.entregables, name = 'Entregables'),
    path('curso_formulario', views.curso_formulario, name = 'curso_formulario'),
    path('profesor_formulario', views.profesor_formulario, name ='profesor_formulario'),
    path('busqueda_generacion', views.busqueda_generacion, name ='busqueda_generacion'),
    path('estudiante_formulario', views.estudiante_formulario, name ='estudiante_formulario'),
    path('buscar/', views.buscar),
]

