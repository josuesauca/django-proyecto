from django.shortcuts import render

# Create your views here. 


from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout




from .forms import FormularioCooperativa
from .forms import FormularioBus
from .forms import FormularioTarjeta



from .models import Cooperativa
from .models import Bus
from .models import Tarjeta

def PaginaInicio(request):
    return render(request, 'index.html', {})


class AccionesUsuario(HttpRequest):
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
    
    def registro_pasajero(request):



class GestionarCooperativa(HttpRequest):

    def agregar_cooperativa(request):
        cooperativa = FormularioCooperativa()
        cooperativas = Cooperativa.objects.all()

        if request.method == 'POST':
            formulario = FormularioCooperativa(data=request.POST)
            if formulario.is_valid():
                formulario.save()
        return render(request,"Cooperativa/IngresarCooperativa.html",{"form":cooperativa,"cooperativas":cooperativas})

    def editar_cooperativa(request,id):
        cooperativa = Cooperativa.objects.get(pk=id)
        form = FormularioCooperativa(instance=cooperativa)
        return render(request, "Cooperativa/EditarCooperativa.html",{"form":form, "cooperativa":cooperativa})

    def actualizar_cooperativa(request,id):
        proveedor = Cooperativa.objects.get(pk=id)
        formulario = FormularioCooperativa(request.POST,instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrarCooperativas")

    def eliminar_cooperativa(request,id):
        proveedor = Cooperativa.objects.get(pk=id)
        proveedor.delete()
        return redirect(to="administrarCooperativas")
        
class GestionarBus(HttpRequest):

    def agregar_bus(request):
        bus = FormularioBus()
        buses = Bus.objects.all()

        if request.method == 'POST':
            formulario = FormularioBus(data=request.POST)
            if formulario.is_valid():
                formulario.save()
        return render(request,"Bus/IngresarBus.html",{"form":bus,"buses":buses})

    def editar_bus(request,id):
        bus = Bus.objects.get(pk=id)
        form = FormularioBus(instance=bus)
        return render(request, "Bus/EditarBus.html",{"form":form, "bus":bus})

    def actualizar_bus(request,id):
        bus = Bus.objects.get(pk=id)
        formulario = FormularioBus(request.POST,instance=bus)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrarBuses")

    def eliminar_bus(request,id):
        bus = Bus.objects.get(pk=id)
        bus.delete()
        return redirect(to="administrarBuses")
        
        
class GestionarTarjeta(HttpRequest):

    def agregar_tarjeta(request):
        tarjeta = FormularioTarjeta()
        tarjetas = Tarjeta.objects.all()

        if request.method == 'POST':
            formulario = FormularioTarjeta(data=request.POST)
            
            if formulario.is_valid():
                formulario.save()

        return render(request,"Tarjeta/IngresarTarjeta.html",{"form":tarjeta,"tarjetas":tarjetas})

    def editar_tarjeta(request,id):
        tarjeta = Tarjeta.objects.get(pk=id)
        form = FormularioTarjeta(instance=tarjeta)
        return render(request, "Tarjeta/EditarTarjeta.html",{"form":form, "tarjeta":tarjeta})

    def actualizar_tarjeta(request,id):
        tarjeta = Tarjeta.objects.get(pk=id)
        formulario = FormularioTarjeta(request.POST,instance=tarjeta)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrarTarjetas")

    def eliminar_tarjeta(request,id):
        tarjeta = Tarjeta.objects.get(pk=id)
        tarjeta.delete()
        return redirect(to="administrarTarjetas")
        