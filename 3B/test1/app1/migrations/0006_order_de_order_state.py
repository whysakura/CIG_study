# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-19 02:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20160219_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_de',
            name='order_state',
            field=models.CharField(default='0', max_length=40),
        ),
    ]
