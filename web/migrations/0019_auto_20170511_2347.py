# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-11 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20170503_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='seating_pattern',
            field=models.CharField(choices=[('BUS_35', 'BUS_35'), ('BUS_31', 'BUS_31')], max_length=50),
        ),
    ]
