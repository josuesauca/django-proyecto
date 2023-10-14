from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Tarjeta(models.Model):
    idTarjeta = models.AutoField(primary_key=True)
    numTarjeta = models.IntegerField(null=True)
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
        return f"Pasajero : {self.nombres}"

@receiver(post_save,sender=User)
def create_profile(sender, instance,created, **kwargs):
    if created:
        Pasajero.objects.create(idUsuario=instance)
        print("Profile created")

#post_save.connect(create_profile, sender=User)

@receiver(post_save,sender=User)
def update_profile(sender, instance,created,**kwargs):
    if created == False:
        instance.pasajero.save()
        print('Profile updated')

#post_save.connect(update_profile, sender=User)

class Cooperativa(models.Model):
    idCooperativa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30,null=True)
    direccion = models.CharField(max_length=30,null=True)
    capacidad = models.IntegerField(null=True)
    
    def __str__(self):
        return f"Cooperativa : {self.nombre}"

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
    
    def __str__(self):
        return f"Bus de la {self.idCooperativa}"

class Viaje(models.Model):
    idPasajero = models.ForeignKey(Pasajero,null=True,on_delete=models.CASCADE)
    idBus = models.ForeignKey(Bus,null=True,on_delete=models.CASCADE)
    costoViaje = models.DecimalField(max_digits= 6,decimal_places=2,null=True) 
    destino = models.CharField(max_length=50,null=True) 

    def __str__(self):
        return f"Viaje a {self.destino}"
    