# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 06:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_remove_robot_1_d'),
    ]

    operations = [
        migrations.RenameField(
            model_name='robot_1',
            old_name='date',
            new_name='dat',
        ),
        migrations.RenameField(
            model_name='robot_1',
            old_name='state',
            new_name='stat',
        ),
    ]
