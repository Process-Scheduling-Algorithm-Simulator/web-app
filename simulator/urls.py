from . import views
from django.urls import path


app_name = 'simulator'
urlpatterns = [
    path('', views.get_index, name='get_index'),
    path('cpuAlgo/',views.cpuScehdular, name='cpuScehdular'),
    path('cpuAlgo/<int:id>/', views.cpuAlgo, name='cpuAlgo'),
    path('sockets/',views.sockets, name='sockets'),
    path('sockets/tcp', views.tcp, name='tcp'),
    path('sockets/udp', views.udp, name='udp')
]