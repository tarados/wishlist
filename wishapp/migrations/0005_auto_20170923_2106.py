# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-23 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishapp', '0004_auto_20170922_1932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desire',
            name='desire_date',
        ),
        migrations.AlterField(
            model_name='desire',
            name='desire_text',
            field=models.TextField(verbose_name='Desire text'),
        ),
    ]