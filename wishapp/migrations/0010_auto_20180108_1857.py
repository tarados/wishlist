# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-08 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishapp', '0009_auto_20180105_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desire',
            name='desire_title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]