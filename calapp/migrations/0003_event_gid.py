# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-28 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calapp', '0002_auto_20161027_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='gid',
            field=models.CharField(default='', max_length=100),
        ),
    ]
