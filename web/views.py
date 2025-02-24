from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import CustomRequest
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

def custom_form_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        description = request.POST.get('description')

        try: 
            CustomRequest.objects.create(email=email, description=description)
            return JsonResponse({"message": "Solicitud recibida correctamente. Gracias por tu interés."})
        except Exception as e:
            return JsonResponse({"message": f"Hubo un problema al guardar los datos: {str(e)}"})
        
    return render(request, 'web/custom_form.html')