# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-17 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishapp', '0012_auto_20180317_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desire',
            name='desire_photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]
