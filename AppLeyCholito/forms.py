from django import forms
from .models import Denuncia
from .models import Authentication
from .models import Login

TIPOS_OPCIONES = (('AC','Abandono en la Calle'),
                      ('ETE','Exposición a Temperaturas Extremas'),
                      ('FA','Falta de Agua'),('FC','Falta de Comida'),
                      ('V','Violencia'),('VA','Venta Ambulante'))
TIPOS_SEXO =(('H', "Hembra"), ('M', "Macho"))
TIPOS_ANIMALES =(('Perro','Perro'),('Gato','Gato'),('Otro','Otro'))

user_type_options = (('PN', 'Persona Natural'),
                 ('RM', 'Representante de Municipalidad'))

class DenunciaForm(forms.ModelForm):
    TipDenuncia = forms.ChoiceField(choices=TIPOS_OPCIONES, widget=forms.Select(attrs={"class": "form-control"}))
    Animal = forms.ChoiceField(choices=TIPOS_ANIMALES, widget=forms.Select(attrs={"class": "form-control"}))
    Sexo = forms.ChoiceField(TIPOS_SEXO, widget=forms.Select(attrs={"class": "form-control"}))
    Color = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            'size': '10',
            'class': 'form-control',
            'placeholder': 'Color del animal...'
        }
    ))
    Comentario = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Descripción extra de la situación...'
        }
    ))
    Herido = forms.BooleanField(required=False, label='<strong>¿Herido?</strong>')

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