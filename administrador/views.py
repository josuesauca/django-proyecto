from django.shortcuts import render

# Create your views here. 


from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render, redirect




from .forms import FormularioCooperativa
from .forms import FormularioBus


from .models import Cooperativa
from .models import Bus

def PaginaInicio(request):
    return render(request, 'index.html', {})


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
        