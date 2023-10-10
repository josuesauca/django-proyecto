from django import forms
from .models import Cooperativa
from .models import Bus
from .models import Tarjeta

class FormularioCooperativa(forms.ModelForm):
    class Meta:
        model = Cooperativa
        fields = "__all__"


class FormularioBus(forms.ModelForm):
    class Meta:
        model = Bus
        fields = "__all__"

class FormularioTarjeta(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = "__all__"