# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app8', '0009_auto_20160108_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_3',
            name='robot',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='data_4',
            name='robot',
            field=models.IntegerField(default=4),
        ),
    ]
