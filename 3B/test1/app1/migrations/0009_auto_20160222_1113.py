# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-22 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20160219_1256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='down_time',
        ),
        migrations.AddField(
            model_name='order',
            name='work_type',
            field=models.CharField(blank=True, default='', max_length=40),
        ),
    ]