# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-05 01:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app7', '0002_book_shuzi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('a', 'achar'), ('s', 'sakura'), ('l', 'love')], max_length=1)),
            ],
        ),
    ]
