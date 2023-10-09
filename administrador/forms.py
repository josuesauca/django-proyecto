from django import forms
from .models import Cooperativa

class FormularioCooperativa(forms.ModelForm):
    class Meta:
        model = Cooperativa
        fields = "__all__"