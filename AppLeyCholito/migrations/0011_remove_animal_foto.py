# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 01:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppLeyCholito', '0010_auto_20171021_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='Foto',
        ),
    ]
