from django import forms
from .models import Denuncia
from .models import Authentication
from .models import Login

TIPOS_SEXO=(('H', "Hembra"), ('M', "Macho"))
user_type_options = (('PN', 'Persona Natural'),
                 ('RM', 'Representante de Municipalidad'))

class DenunciaForm(forms.ModelForm):
    #Herido = forms.BooleanField(default=False)
    Sexo = forms.MultipleChoiceField(required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=TIPOS_SEXO,
    )
    class Meta:
        model = Denuncia
        fields = ('TipDenuncia', 'Animal', 'Sexo', 'Herido', 'Color', 'Comentario')


class AuthenticationForm(forms.ModelForm):
    class Meta:
        model = Authentication
        widgets = {
            'password': forms.PasswordInput(),
            'password_repeat': forms.PasswordInput(),
        }
        fields = ('username', 'password', 'password_repeat', 'user_type')


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        widgets = {
            'password': forms.PasswordInput(),
        }
        fields = ('username', 'password')

