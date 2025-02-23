from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return render(request, 'web/index.html')  # Cambia si deseas otra página como inicio

def pre_build(request):
    return render(request, 'web/pre_build.html')

def custom_case(request):
    return render(request, 'web/custom_case.html')

def cus_view(request):
    return render(request, 'web/Cus.html')

def pre_build_gaming(request):
    return render(request, 'web/pre_build_Gaming.html')

def pre_build_escuela(request):
    return render(request, 'web/pre_build_Escuela.html')

def pre_build_trabajo(request):
    return render(request, 'web/pre_build_Trabajo.html')

def navbar_view(request):
    return render(request, 'web/navbar.html')