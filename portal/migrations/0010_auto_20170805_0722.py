# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_auto_20170805_0722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='marital_status',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'married'), (1, 'single')], null=True),
        ),
        migrations.AlterField(
            model_name='usersession',
            name='sessionid',
            field=models.TextField(default='e737c0c6071643c8878603dd9d6f7c3a', max_length=100, primary_key=True, serialize=False),
        ),
    ]
