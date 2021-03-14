from . import views
from django.urls import path


app_name = 'simulator'
urlpatterns = [
    path('', views.get_index, name='get_index'),
    path('cpuAlgo/<int:id>/', views.cpuSchedular, name='cpuSchedular'),
]