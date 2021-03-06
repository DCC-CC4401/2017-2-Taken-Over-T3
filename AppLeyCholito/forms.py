# -*- coding: utf-8 -*-
from django import forms
from .models import Denuncia
from .models import Authentication
from .models import Login
from .models import Animal
import datetime
from django.contrib.auth.models import User
from django.forms import extras


TIPOS_OPCIONES = (('AC','Abandono en la Calle'),
                      ('ETE','Exposición a Temperaturas Extremas'),
                      ('FA','Falta de Agua'),('FC','Falta de Comida'),
                      ('V','Violencia'),('VA','Venta Ambulante'))
TIPOS_SEXO =(('H', "Hembra"), ('M', "Macho"))
TIPOS_ANIMALES =(('Perro','Perro'),('Gato','Gato'),('Otro','Otro'))

user_type_options = (('PN', 'Persona Natural'),
                 ('RM', 'Representante de Municipalidad'),
                         ('RO','Representante de Organizacion'),
                         ('ADM','Administrador'))

TIPOS_ESTADO = (('reportadas','reportadas'), ('consolidadas','consolidadas'),
                    ('verificadas','verificadas'),('cerradas','cerradas'),
                    ('desechadas','desechadas'))

class AnimalForm(forms.ModelForm):
    Nombre = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            'size': '10',
            'class': 'form-control'
        }
    ))
    Foto = forms.ImageField()
    Sexo = forms.ChoiceField(choices=TIPOS_SEXO, widget=forms.Select(attrs={"class": "form-control"}))
    Tipo = forms.ChoiceField(choices=TIPOS_ANIMALES, widget=forms.Select(attrs={"class": "form-control"}))
    Edad_Estimda = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    En_adopcion_desde = forms.DateField(widget=extras.SelectDateWidget(attrs={'class': 'form-control'}))
    Adoptado = forms.BooleanField(required=False)
    Comentario = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Añadir descripción...",
        'rows': 4,
        'cols': 15
    }))
    class Meta:
       model= Animal
       fields=("Nombre", "Foto", "Sexo", "Tipo", "Edad_Estimda", "En_adopcion_desde", "Adoptado", "Comentario")

class DenunciaForm(forms.ModelForm):
    TipDenuncia = forms.ChoiceField(choices=TIPOS_OPCIONES, widget=forms.Select(
        attrs={
            "class": "form-control",
        })
    )
    Animal = forms.ChoiceField(choices=TIPOS_ANIMALES, widget=forms.Select(attrs={"class": "form-control"}))
    Sexo = forms.ChoiceField(TIPOS_SEXO, widget=forms.Select(attrs={"class": "form-control"}))
    Color = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            'size': '10',
            'class': 'form-control',
            'placeholder': 'Color del animal...'
        }
    ))
    Comentario = forms.CharField(max_length=100, widget=forms.TextInput(
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
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        }
    ))
    password_repeat = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Repite la Contraseña'
        }
    ))
    user_type = forms.ChoiceField(choices=user_type_options, widget=forms.Select(
        attrs={
            "class": "form-control",
        })
                                    )
    class Meta:
        model = Authentication
        fields = ('username', 'password', 'password_repeat', 'user_type')

class LoginForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        }
    ))
    class Meta:
        model = Login
        fields = ('username', 'password')


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Usuario'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class DenunciaForm1(forms.ModelForm):
    TipDenuncia = forms.ChoiceField(choices=TIPOS_OPCIONES, widget=forms.Select(
        attrs={
            "class": "form-control",
        })
    )
    Animal = forms.ChoiceField(choices=TIPOS_ANIMALES, widget=forms.Select(attrs={"class": "form-control"}))
    Sexo = forms.ChoiceField(TIPOS_SEXO, widget=forms.Select(attrs={"class": "form-control"}))
    Color = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            'size': '10',
            'class': 'form-control',
            'placeholder': 'Color del animal...'
        }
    ))
    Comentario = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Descripción extra de la situación...'
        }
    ))
    Herido = forms.BooleanField(required=False)
    TIPOS_ESTADO = forms.ChoiceField(choices=TIPOS_ESTADO, widget=forms.Select(attrs={"class": "form-control"}), required=False)
    class Meta:
        model = Denuncia
        fields = ('TipDenuncia', 'Animal', 'Sexo', 'Herido', 'Color', 'Comentario', 'TIPOS_ESTADO')
