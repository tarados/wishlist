# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishapp', '0003_desire_desire_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='desire',
            name='desire_img',
            field=models.TextField(null=True),
        ),
    ]
