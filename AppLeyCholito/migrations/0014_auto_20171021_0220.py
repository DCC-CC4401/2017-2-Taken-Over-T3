# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLeyCholito', '0013_auto_20171021_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='Foto',
            field=models.ImageField(default=b'in.jpeg', upload_to=b'AppLeyCholito/images'),
        ),
    ]
