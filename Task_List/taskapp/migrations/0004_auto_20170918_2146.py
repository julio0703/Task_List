# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0003_auto_20170918_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='text',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
