# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-04 01:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test2', '0009_auto_20160203_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='next_fu',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='nextf', to='test2.Mark'),
        ),
        migrations.AlterField(
            model_name='mark',
            name='next_main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nextm', to='test2.Mark'),
        ),
    ]
