# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0012_auto_20160120_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='car_number',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, to='test1.Car'),
        ),
    ]