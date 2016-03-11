# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 01:58
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
                ('car_number', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goods_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=40)),
                ('goods_type', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Linebody',
            fields=[
                ('line_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('station_number', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(max_length=40)),
                ('order_time', models.CharField(max_length=40)),
                ('order_state', models.CharField(default='未完成', max_length=40)),
                ('down_time', models.CharField(blank=True, max_length=50)),
                ('finish_time', models.CharField(blank=True, default='', max_length=40)),
                ('total_time', models.CharField(blank=True, default='', max_length=40)),
                ('car_number', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='test2.Car')),
                ('line_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test2.Linebody')),
            ],
        ),
        migrations.CreateModel(
            name='Order_de',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='', max_length=40)),
                ('goods_count', models.CharField(max_length=40)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test2.Goods')),
                ('order_sn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test2.Order')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('sta_number', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('sta_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car_state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test2.State'),
        ),
    ]