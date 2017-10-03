# -*- coding: utf-8 -*-
from django.db import models

class Denuncia(models.Model):
    TIPOS_OPCIONES = (('AC','Abandono en la Calle'),
                      ('ETE','Exposición a Temperaturas Extremas'),
                      ('FA','Falta de Agua'),('FC','Falta de Comida'),
                      ('V','Violencia'),('VA','Venta Ambulante'))
    TIPOS_ANIMALES=(('Perro','Perro'),('Gato','Gato'),('Otro','Otro'))
    TIPOS_SEXO=(('H',"Hembra"),('M',"Macho"))
    TipDenucia=models.CharField(max_length=3,choices=TIPOS_OPCIONES)
    Animal=models.CharField(max_length=10,choices=TIPOS_ANIMALES)
    Sexo=models.CharField(max_length=1,choices=TIPOS_SEXO)
    Color= models.CharField(max_length=10)
    Herido= models.BooleanField
    Comentario= models.CharField(max_length=30)
