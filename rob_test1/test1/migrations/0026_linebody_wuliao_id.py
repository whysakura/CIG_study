# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-26 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0025_auto_20160121_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='linebody',
            name='wuliao_id',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
