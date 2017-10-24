# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLeyCholito', '0005_auto_20171019_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=15)),
                ('Sexo', models.CharField(choices=[(b'H', b'Hembra'), (b'M', b'Macho')], max_length=1)),
                ('Tipo', models.CharField(choices=[(b'Perro', b'Perro'), (b'Gato', b'Gato'), (b'Otro', b'Otro')], max_length=10)),
                ('Adoptado', models.BooleanField()),
                ('Comentario', models.CharField(max_length=200)),
            ],
        ),
    ]
