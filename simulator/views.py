from django.shortcuts import render
from .models import *

# Create your views here.

def get_index(request):
    return render(request, 'index.html')

def cpuScehdular(request):
    return render(request, 'cpuAlgos/cpu_main.html')

def cpuAlgo(request, id):
    algo = CpuAlgo.objects.filter(algo_id=id)[0]
    return render(request, 'cpuAlgos/cpu_algo.html', {'algo': algo})

def sockets(request):
    return render(request, 'sockets/sockets_main.html')

def tcp(request):
    return render(request, 'sockets/tcp.html')

def udp(request):
    return render(request, 'sockets/udp.html')