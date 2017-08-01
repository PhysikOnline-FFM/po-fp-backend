# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpraktikum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='graduation',
            field=models.CharField(blank=True, choices=[('BA', 'Bachelor'), ('MA', 'Master'), ('L', 'Lehramt')], max_length=2),
        ),
        migrations.AlterField(
            model_name='fpregistration',
            name='semester',
            field=models.CharField(blank=True, default='WS17', max_length=4, verbose_name='semester'),
        ),
    ]
