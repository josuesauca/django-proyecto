from django.shortcuts import render

# Create your views here. 

from decimal import Decimal
import random

from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test

from .forms import FormularioCooperativa
from .forms import FormularioBus
from .forms import FormularioTarjeta
from .forms import FormularioViaje

from .models import Cooperativa
from .models import Bus
from .models import Tarjeta
from .models import Pasajero
from .models import Viaje

from .decorators import unauthenticated_user, allowed_user, admin_only

def PaginaInicio(request):
    return render(request, 'index.html', {})

def check_admin(user):
   return user.is_superuser

class GestionarViaje(HttpRequest):
    @unauthenticated_user

    def agregar_viaje(request):
        viaje = FormularioViaje()
        viajes = Viaje.objects.all()
        if request.method == 'POST':

            pasajero_encontrado = Pasajero.objects.filter(idUsuario=request.user.id).first()
            
            bus_encontrado = Bus.objects.filter(idBus=int(request.POST.get('idBus'))).first()
            
            if pasajero_encontrado.idTarjeta.saldoTarjeta > Decimal(request.POST.get('costoViaje')):

                pasajero_encontrado.idTarjeta.saldoTarjeta = pasajero_encontrado.idTarjeta.saldoTarjeta - Decimal(request.POST.get('costoViaje'))
                
                print("slga",pasajero_encontrado.idTarjeta.saldoTarjeta)
                
                #pasajero_encontrado.up

                user = Viaje.objects.create(idPasajero = pasajero_encontrado,
                                            idBus = bus_encontrado ,
                                            costoViaje = Decimal(request.POST.get('costoViaje')),
                                            destino = request.POST.get('destino'))
                user.save()
        return render(request,"Viaje/Viajes.html",{"form":viaje,"viajes":viajes})

class AccionesUsuario(HttpRequest):

    @unauthenticated_user
    def log_in(request):
        if(request.method == "POST"):
            user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
            if user is None:
                messages.error(request,"Usuario no encontrado")
                return redirect("login")
            else:
                login(request, user)
                return redirect("index")
        else:
            return render(request, "Usuario/Login.html",{})
            
    def log_out(request):
        logout(request)
        return redirect("index")
    
    def registro_usuario(request):
        if(request.method == "POST"):
            if request.POST["password1"] == request.POST["password2"]:
                username = request.POST['username']
                email = request.POST['email']
                password1 = request.POST['password1']
                user = User.objects.create_user(
                        username=username, password=password1, email=email)
            user.save()
            return redirect("registrarPasajero")
        else:
            return render(request, "Usuario/Usuario.html",{})
    
    def registro_pasajero(request):
        if(request.method == "POST"):
            nombres_completos = request.POST['full_name']
            cedula = request.POST['cedula']
            user = User.objects.last()

            my_group = Group.objects.get(name='clientes') 
            my_group.user_set.add(user)

            #Crear tarjeta para el pasajero
            tarjeta = Tarjeta.objects.create(numTarjeta =random.randint(10000,100000), saldoTarjeta=0.0)
            tarjeta.save()

            tarjeta_guardada = Tarjeta.objects.last()

            pasajero = Pasajero.objects.create(idUsuario = user, nombres=nombres_completos, cedula=cedula, idTarjeta = tarjeta_guardada)
            pasajero.save()

            return redirect("login")
        else:
            return render(request, "Usuario/PerfilPasajero.html",{})
        
    def ver_informacion_pasajero(request):
        current_user = Pasajero.objects.get(idUsuario=request.user)
        return render(request, "Pasajero/InformacionPasajero.html",{'usuario':current_user})

class GestionarCooperativa(HttpRequest):

    #@allowed_user(allowed_roles=['admin'])
    @admin_only
    def agregar_cooperativa(request):
        cooperativa = FormularioCooperativa()
        cooperativas = Cooperativa.objects.all()

        if request.method == 'POST':
            formulario = FormularioCooperativa(data=request.POST)
            if formulario.is_valid():
                formulario.save()
        return render(request,"Cooperativa/IngresarCooperativa.html",{"form":cooperativa,"cooperativas":cooperativas})

    @admin_only
    def editar_cooperativa(request,id):
        cooperativa = Cooperativa.objects.get(pk=id)
        form = FormularioCooperativa(instance=cooperativa)
        return render(request, "Cooperativa/EditarCooperativa.html",{"form":form, "cooperativa":cooperativa})

    @admin_only
    def actualizar_cooperativa(request,id):
        proveedor = Cooperativa.objects.get(pk=id)
        formulario = FormularioCooperativa(request.POST,instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrarCooperativas")
    
    @admin_only
    def eliminar_cooperativa(request,id):
        proveedor = Cooperativa.objects.get(pk=id)
        proveedor.delete()
        return redirect(to="administrarCooperativas")

class GestionarBus(HttpRequest):

    @admin_only
    def agregar_bus(request):
        bus = FormularioBus()
        buses = Bus.objects.all()

        if request.method == 'POST':
            formulario = FormularioBus(data=request.POST)
            if formulario.is_valid():
                formulario.save()
        return render(request,"Bus/IngresarBus.html",{"form":bus,"buses":buses})

    @admin_only
    def editar_bus(request,id):
        bus = Bus.objects.get(pk=id)
        form = FormularioBus(instance=bus)
        return render(request, "Bus/EditarBus.html",{"form":form, "bus":bus})
    
    @admin_only
    def actualizar_bus(request,id):
        bus = Bus.objects.get(pk=id)
        formulario = FormularioBus(request.POST,instance=bus)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrarBuses")
        
    @admin_only
    def eliminar_bus(request,id):
        bus = Bus.objects.get(pk=id)
        bus.delete()
        return redirect(to="administrarBuses")
        
class GestionarTarjeta(HttpRequest):

    @admin_only
    def agregar_tarjeta(request):
        tarjeta = FormularioTarjeta()
        tarjetas = Tarjeta.objects.all()

        if request.method == 'POST':
            formulario = FormularioTarjeta(data=request.POST)
            
            if formulario.is_valid():
                formulario.save()

        return render(request,"Tarjeta/IngresarTarjeta.html",{"form":tarjeta,"tarjetas":tarjetas})

    @admin_only
    def editar_tarjeta(request,id):
        tarjeta = Tarjeta.objects.get(pk=id)
        form = FormularioTarjeta(instance=tarjeta)
        return render(request, "Tarjeta/EditarTarjeta.html",{"form":form, "tarjeta":tarjeta})
    
    @admin_only
    def actualizar_tarjeta(request,id):
        tarjeta = Tarjeta.objects.get(pk=id)
        formulario = FormularioTarjeta(request.POST,instance=tarjeta)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrarTarjetas")
        
    @admin_only
    def eliminar_tarjeta(request,id):
        tarjeta = Tarjeta.objects.get(pk=id)
        tarjeta.delete()
        return redirect(to="administrarTarjetas")

"""
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def correo(request,id):

    email = EmailMessage(

    )
"""

