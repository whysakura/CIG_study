# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_auto_20160113_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Now_time1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=100)),
            ],
        ),
    ]