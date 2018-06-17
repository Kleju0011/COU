# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-16 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city_engine', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('income', models.IntegerField()),
                ('health', models.IntegerField()),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city_engine.City')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.ContentType')),
                ('resident', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='city_engine.Residential')),
            ],
        ),
    ]
