# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0019_auto_20160120_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='down_time',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
