from django import forms
from .models import Cooperativa
from .models import Bus

class FormularioCooperativa(forms.ModelForm):
    class Meta:
        model = Cooperativa
        fields = "__all__"


class FormularioBus(forms.ModelForm):
    class Meta:
        model = Bus
        fields = "__all__"