# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_remove_robot_1_d'),
    ]

    operations = [
        migrations.AddField(
            model_name='robot_1',
            name='d',
            field=models.CharField(default=33, max_length=33),
        ),
    ]