from django.shortcuts import render
from .models import *

# Create your views here.

def get_index(request):
    return render(request, 'index.html')
    

# CPU scheduling
def cpuScehdular(request):
    return render(request, 'cpuAlgos/cpu_main.html')

def cpuAlgo(request, id):
    algo = CpuAlgo.objects.filter(algo_id=id)[0]
    return render(request, 'cpuAlgos/cpu_algo.html', {'algo': algo})

def cpu_quiz(request):
    return render(request, 'cpuAlgos/cpu_quiz.html')




# Sockets
def sockets(request):
    return render(request, 'sockets/sockets_main.html')

def tcp(request):
    return render(request, 'sockets/tcp.html')

def udp(request):
    return render(request, 'sockets/udp.html')

def sockets_quiz(request):
    return render(request, 'sockets/sockets_quiz.html')




# Election Algorithms
def election(request):
    return render(request, 'election/election_main.html')

def bully(request):
    return render(request, 'election/bully.html')

def ring(request):
    return render(request, 'election/ring.html')

def election_quiz(request):
    return render(request, 'election/election_quiz.html')