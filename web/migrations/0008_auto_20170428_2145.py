# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-28 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_bus_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='price',
            field=models.IntegerField(),
        ),
    ]
