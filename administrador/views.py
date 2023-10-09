from django.shortcuts import render

# Create your views here. 


from django.http import HttpResponse
from django.http import HttpRequest



from .forms import FormularioCooperativa


from .models import Cooperativa

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
        proveedor = Proveedor.objects.get(id=id)
        form = FormularioProveedor(instance=proveedor)
        return render(request, "Administrador/EditarProveedor.html",{"form":form, "proveedor":proveedor})

    def actualizar_cooperativa(request,id):
        proveedor = Proveedor.objects.get(pk=id)
        formulario = FormularioProveedor(request.POST,instance=proveedor)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="administrarProveedores")

    def eliminar_cooperativa(request,id):
        proveedor = Proveedor.objects.get(pk=id)
        proveedor.delete()
        return redirect(to="administrarProveedores")
        