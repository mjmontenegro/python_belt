# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-21 19:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
