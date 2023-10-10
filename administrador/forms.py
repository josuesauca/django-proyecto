from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class FormularioUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

    def __init__(self, *args, **kwargs):
        super(FormularioUsuario, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None