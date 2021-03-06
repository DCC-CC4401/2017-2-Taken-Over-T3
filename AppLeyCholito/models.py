# -*- coding: utf-8 -*-
from django.db import models
import datetime
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")


class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Authentication(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    password_repeat = models.CharField(max_length=20)
    user_type_options = (('PN', 'Persona Natural'),
                 ('RM', 'Representante de Municipalidad'),
                         ('RO','Representante de Organizacion'),
                         ('ADM','Administrador'))
    user_type = models.CharField(max_length=1, choices=user_type_options)

class Animal(models.Model):
    TIPOS_ANIMALES = (('Perro', 'Perro'), ('Gato', 'Gato'), ('Otro', 'Otro'))
    TIPOS_SEXO = (('H', "Hembra"), ('M', "Macho"))
    Nombre = models.CharField(max_length=15)
    Foto = models.ImageField(upload_to='AppLeyCholito/static/AppLeyCholito/imgs_animales', default='in.jpeg')
    Sexo = models.CharField(max_length=1, choices=TIPOS_SEXO)
    Tipo = models.CharField(max_length=10, choices=TIPOS_ANIMALES)
    Adoptado = models.BooleanField()
    Edad_Estimda= models.IntegerField(default=0, max_length=3)
    En_adopcion_desde= models.DateField(default=datetime.date.today())
    Comentario = models.CharField(max_length=200)

class Denuncia(models.Model):
    TIPOS_OPCIONES = (('AC','Abandono en la Calle'),
                      ('ETE','Exposicion a Temperaturas Extremas'),
                      ('FA','Falta de Agua'),('FC','Falta de Comida'),
                      ('V','Violencia'),('VA','Venta Ambulante'))
    TIPOS_ANIMALES =(('Perro','Perro'),('Gato','Gato'),('Otro','Otro'))
    TIPOS_SEXO = (('H',"Hembra"),('M',"Macho"))
    TIPOS_ESTADO = (('reportadas','reportadas'), ('consolidadas','consolidadas'),
                    ('verificadas','verificadas'),('cerradas','cerradas'),
                    ('desechadas','desechadas'))

    TipDenuncia = models.CharField(max_length=3, choices=TIPOS_OPCIONES)
    Estado_Denuncia = models.CharField(max_length=10, choices=TIPOS_ESTADO)
    Animal = models.CharField(max_length=10, choices=TIPOS_ANIMALES)
    Sexo = models.CharField(max_length=1, choices=TIPOS_SEXO)
    Color = models.CharField(max_length=10)
    Herido = models.BooleanField()
    Comentario = models.CharField(max_length=30)

    def get_animal_type(self):
        if self.TIPOS_ANIMALES == "AC":
            return "Abandono en la Calle"
        elif self.TIPOS_ANIMALES == "FC":
            return "Falta de Comida"
        elif self.TIPOS_ANIMALES == "ETE":
            return "Exposicion a Temperaturas Extremas"
        elif self.TIPOS_ANIMALES == "FA":
            return "Falta de Agua"
        elif self.TIPOS_ANIMALES == "V":
            return "Violencia"
        elif self.TIPOS_ANIMALES == "VA":
            return "Venta Ambulante"
