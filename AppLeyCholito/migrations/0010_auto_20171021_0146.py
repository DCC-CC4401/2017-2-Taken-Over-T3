# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLeyCholito', '0009_remove_animal_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='Foto',
            field=models.ImageField(default=b'in.jpeg', upload_to=b'AppLeyCholito/images'),
        ),
        migrations.AlterField(
            model_name='denuncia',
            name='TipDenuncia',
            field=models.CharField(choices=[(b'AC', b'Abandono en la Calle'), (b'ETE', b'Exposicion a Temperaturas Extremas'), (b'FA', b'Falta de Agua'), (b'FC', b'Falta de Comida'), (b'V', b'Violencia'), (b'VA', b'Venta Ambulante')], max_length=3),
        ),
    ]
