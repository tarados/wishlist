# Generated by Django 2.0.7 on 2018-08-05 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishapp', '0018_auto_20180805_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desire',
            name='desire_substitute_id',
            field=models.CharField(default='', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='desirelist',
            name='desirelist_substitute_id',
            field=models.CharField(default='', max_length=8, unique=True),
        ),
    ]
