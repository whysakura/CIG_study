# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app8', '0007_auto_20160108_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='data_2',
            name='robot',
            field=models.IntegerField(default=1),
        ),
    ]
