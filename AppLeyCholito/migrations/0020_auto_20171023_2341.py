# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLeyCholito', '0019_auto_20171023_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncia',
            name='Estado_Denuncia',
            field=models.CharField(choices=[('reportadas', 'reportadas'), ('consolidadas', 'consolidadas'), ('verificadas', 'verificadas'), ('cerradas', 'cerradas'), ('desechadas', 'desechadas')], max_length=10),
        ),
    ]