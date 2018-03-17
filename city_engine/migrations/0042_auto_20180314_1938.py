# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-14 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_engine', '0041_auto_20180305_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coalplant',
            name='total_energy_production',
        ),
        migrations.RemoveField(
            model_name='ropeplant',
            name='total_energy_production',
        ),
        migrations.RemoveField(
            model_name='windplant',
            name='total_energy_production',
        ),
        migrations.AlterField(
            model_name='residential',
            name='max_population',
            field=models.PositiveIntegerField(default=30),
        ),
    ]
