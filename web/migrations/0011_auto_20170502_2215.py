# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-02 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20170502_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='seating_pattern',
            field=models.CharField(choices=[([[1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 0, 0], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 1, 1]], 'BUS_35'), ([[1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 0, 0], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1], [1, 1, 0, 1, 1]], 'BUS_31')], default='BUS_35', max_length=50),
        ),
    ]
