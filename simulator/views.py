from django.shortcuts import render
from .models import *

# Create your views here.

def get_index(request):
    return render(request, 'index.html')

def cpuSchedular(request, id):
    algo = CpuAlgo.objects.filter(algo_id=id)[0]
    return render(request, 'cpuAlgos/cpu.html', {'algo': algo})
