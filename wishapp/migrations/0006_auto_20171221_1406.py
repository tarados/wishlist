# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-21 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishapp', '0005_auto_20171213_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desire',
            name='desire_text',
            field=models.TextField(max_length=30),
        ),
    ]
