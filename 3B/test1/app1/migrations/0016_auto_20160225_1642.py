# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 08:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_auto_20160225_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mark',
            name='next_fu',
        ),
        migrations.RemoveField(
            model_name='mark',
            name='next_main',
        ),
    ]
