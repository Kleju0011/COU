# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-09 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_engine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityfield',
            name='field_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
