# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20170804_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user_roll_no',
            field=models.CharField(default='hello', max_length=20),
            preserve_default=False,
        ),
    ]
