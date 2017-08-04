# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='blood_group',
            field=models.SmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'AB'), (3, 'O')], null=True),
        ),
    ]
