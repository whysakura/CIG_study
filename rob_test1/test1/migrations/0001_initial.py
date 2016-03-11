# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-18 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=40)),
                ('down_time', models.CharField(max_length=50)),
                ('car_sign', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Linebody',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number', models.IntegerField()),
                ('line_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat_name', models.CharField(max_length=40)),
                ('mat_type', models.CharField(max_length=40)),
                ('mat_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sta_number', models.IntegerField()),
                ('sta_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_number', models.IntegerField()),
                ('left_ci', models.CharField(max_length=40)),
                ('right_ci', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test1.State'),
        ),
    ]
