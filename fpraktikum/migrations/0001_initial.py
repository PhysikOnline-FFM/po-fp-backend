# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 11:34
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='course name')),
                ('places', models.IntegerField(blank=True, null=True, verbose_name='places')),
                ('graduation',
                 models.CharField(choices=[('BA', 'Bachelor'), ('MA', 'Master'), ('L', 'Lehramt')], max_length=2)),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
            },
        ),
        migrations.CreateModel(
            name='FpRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(default='WS17', max_length=4, null=True, verbose_name='semester')),
                ('start_date',
                 models.DateTimeField(auto_now_add=True, null=True, verbose_name='startdate of registration')),
                (
                'end_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='enddate of registration')),
            ],
            options={
                'verbose_name': 'FP registration',
                'verbose_name_plural': 'Fp registrations',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='semester_half',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses',
                                    to='fpraktikum.FpRegistration', verbose_name='semester half'),
        ),
    ]
