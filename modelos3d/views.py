from django.shortcuts import render
from .models import Modelo3D
# Create your views here.

def index(request):
    modelos = Modelo3D.objects.all()
    return render(request, 'modelos3d/index.html', {'modelos': modelos})