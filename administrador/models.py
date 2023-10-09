from django.db import models
import random
from django.contrib.auth.models import User

# Create your models here.

class Tarjeta(models.Model):
    idTarjeta = models.AutoField(primary_key=True)
    numTarjeta = models.IntegerField(random.randint(100,10000), null=True, editable=False)
    saldoTarjeta = models.DecimalField(max_digits= 6,decimal_places=2,null=True) 

    def __str__(self):
        return f"Tarjeta : {self.idTarjeta}  , {self.numTarjeta} , {self.saldoTarjeta} "

class Pasajero(models.Model):
    idPasajero = models.AutoField(primary_key=True)
    idTarjeta = models.OneToOneField(Tarjeta,null=True,on_delete=models.CASCADE)
    idUsuario = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    nombres = models.CharField(max_length=30,null=True)
    cedula = models.IntegerField(null=True)

    def __str__(self):
        return f"Pasajero : {self.idPasajero}  , {self.idTarjeta} , {self.idUsuario}, {self.nombres} , {self.cedula}"

class Cooperativa(models.Model):
    idCooperativa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30,null=True)
    direccion = models.CharField(max_length=30,null=True)
    capacidad = models.IntegerField(null=True)
    
    def __str__(self):
        return f"Cooperativa : {self.idCooperativa}  , {self.nombre} , {self.direccion}, {self.capacidad}"

class Bus(models.Model):
    idBus = models.AutoField(primary_key=True)
    idCooperativa = models.OneToOneField(Cooperativa,null=True,on_delete=models.CASCADE)
    propietario = models.CharField(max_length=30,null=True)
    capacidad = models.IntegerField(null=True)
    placa = models.CharField(max_length=10,null=True)

    tiposBus = (
        (1, "Publico"),
        (2, "Escolar"),
        (3, "Turistico"),
    )
    tipo = models.IntegerField(choices=tiposBus, default=1)

class Viaje(models.Model):
    idPasajero = models.ForeignKey(Pasajero,null=True,on_delete=models.CASCADE)
    idBus = models.ForeignKey(Bus,null=True,on_delete=models.CASCADE)
    costoViaje = models.DecimalField(max_digits= 6,decimal_places=2,null=True) 
    