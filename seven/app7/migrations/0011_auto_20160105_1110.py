# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 03:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app7', '0010_auto_20160105_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='person',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app7.Author'),
        ),
    ]
