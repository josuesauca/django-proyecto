"""
URL configuration for sistema_bus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

import administrador.views as vistas

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', vistas.PaginaInicio,name='index'),



    #Rutas Cooperativa
    path('administrarCooperativas/', vistas.GestionarCooperativa.agregar_cooperativa ,name='administrarCooperativas'),
    path('editarCooperativas/<int:id>', vistas.GestionarCooperativa.editar_cooperativa ,name='editarCooperativas'),
    path('actualizarCooperativas/<int:id>', vistas.GestionarCooperativa.actualizar_cooperativa ,name='actualizarCooperativas'),
    path('eliminarCooperativas/<int:id>', vistas.GestionarCooperativa.eliminar_cooperativa, name = "eliminarCooperativas"),


]
