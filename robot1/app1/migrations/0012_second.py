# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-14 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_now_time1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Second',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec', models.CharField(max_length=100)),
            ],
        ),
    ]
