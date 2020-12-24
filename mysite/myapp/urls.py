"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.urls import path
from . import views

urlpatterns = [

 path('', views.index, name='index'),
 
 path('estilo/<int:id_estilo>/', views.estilo_detalle, name='estilo_detalle'),
 
 path('interprete/<int:id_interprete>/', views.interprete_detalle, name='interprete_detalle'),
 
 path('cancion/<int:id_cancion>/', views.cancion_detalle, name='cancion_detalle'),

 path('busqueda/', views.BusquedaCancion.as_view(), name='busqueda_canciones')
]
