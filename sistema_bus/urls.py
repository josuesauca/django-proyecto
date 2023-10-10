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
from django.conf import settings
from django.conf.urls.static import static


import administrador.views as vistas

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', vistas.PaginaInicio,name='index'),


    #URLs Usuario
    path('login/', vistas.AccionesUsuario.log_in ,name='login'),
    path('logout/<int:id>', vistas.AccionesUsuario.log_out ,name='logout'),


    #URLs Cooperativa
    path('administrarCooperativas/', vistas.GestionarCooperativa.agregar_cooperativa ,name='administrarCooperativas'),
    path('editarCooperativas/<int:id>', vistas.GestionarCooperativa.editar_cooperativa ,name='editarCooperativas'),
    path('actualizarCooperativas/<int:id>', vistas.GestionarCooperativa.actualizar_cooperativa ,name='actualizarCooperativas'),
    path('eliminarCooperativas/<int:id>', vistas.GestionarCooperativa.eliminar_cooperativa, name = "eliminarCooperativas"),

    #URLs Bus
    path('administrarBuses/', vistas.GestionarBus.agregar_bus ,name='administrarBuses'),
    path('editarBuses/<int:id>', vistas.GestionarBus.editar_bus ,name='editarBuses'),
    path('actualizarBuses/<int:id>', vistas.GestionarBus.actualizar_bus ,name='actualizarBuses'),
    path('eliminarBuses/<int:id>', vistas.GestionarBus.eliminar_bus, name = "eliminarBuses"),

    #URLs Tarjetas
    path('administrarTarjetas/', vistas.GestionarTarjeta.agregar_tarjeta ,name='administrarTarjetas'),
    path('editarTarjetas/<int:id>', vistas.GestionarTarjeta.editar_tarjeta ,name='editarTarjetas'),
    path('actualizarTarjetas/<int:id>', vistas.GestionarTarjeta.actualizar_tarjeta ,name='actualizarTarjetas'),
    path('eliminarTarjetas/<int:id>', vistas.GestionarTarjeta.eliminar_tarjeta, name = "eliminarTarjetas"),


]+ static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
