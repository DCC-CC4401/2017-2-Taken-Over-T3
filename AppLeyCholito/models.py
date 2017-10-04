# -*- coding: utf-8 -*-
from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username + '-' + self.password

class Authentication(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    password_repeat = models.CharField(max_length=20)
    user_type_options = (('PN', 'Persona Natural'),
                 ('RM', 'Representante de Municipalidad'))
    user_type = models.CharField(max_length=1, choices=user_type_options)



class Denuncia(models.Model):
    TIPOS_OPCIONES = (('AC','Abandono en la Calle'),
                      ('ETE','Exposición a Temperaturas Extremas'),
                      ('FA','Falta de Agua'),('FC','Falta de Comida'),
                      ('V','Violencia'),('VA','Venta Ambulante'))
    TIPOS_ANIMALES =(('Perro','Perro'),('Gato','Gato'),('Otro','Otro'))
    TIPOS_SEXO = (('H',"Hembra"),('M',"Macho"))
    TipDenuncia = models.CharField(max_length=3, choices=TIPOS_OPCIONES)
    Animal = models.CharField(max_length=10, choices=TIPOS_ANIMALES)
    Sexo = models.CharField(max_length=1, choices=TIPOS_SEXO)
    Color = models.CharField(max_length=10)
    Herido = models.BooleanField(default=False)
    Comentario = models.CharField(max_length=30)
