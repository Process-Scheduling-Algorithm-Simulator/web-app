from . import views
from django.urls import path


app_name = 'simulator'
urlpatterns = [
    path('', views.get_index, name='get_index'),
    path('cpuAlgo/',views.cpuScehdular, name='cpuScehdular'),
    path('cpuAlgo/<int:id>/', views.cpuAlgo, name='cpuAlgo'),
    path('cpuAlgo/quiz/', views.cpu_quiz, name='cpu_quiz'),

    path('sockets/',views.sockets, name='sockets'),
    path('sockets/tcp/', views.tcp, name='tcp'),
    path('sockets/udp/', views.udp, name='udp'),
    path('sockets/quiz/',views.sockets_quiz, name='sockets_quiz'),

    path('election/',views.election, name='election'),
    path('election/bully/', views.bully, name='bully'),
    path('election/ring/', views.ring, name='ring'),
    path('election/quiz/',views.election_quiz, name='election_quiz'),
]