# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 03:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0010_auto_20160120_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_name',
            new_name='car_number',
        ),
    ]
