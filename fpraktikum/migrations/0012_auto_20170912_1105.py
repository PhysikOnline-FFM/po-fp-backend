# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 11:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fpraktikum', '0011_auto_20170912_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fpuserregistrant',
            name='partner',
        ),
        migrations.AddField(
            model_name='fpuserpartner',
            name='registrant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='partner', to='fpraktikum.FpUserRegistrant', verbose_name='registrant'),
        ),
    ]
