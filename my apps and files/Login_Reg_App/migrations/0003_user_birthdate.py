# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-20 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login_Reg_App', '0002_auto_20190620_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]
