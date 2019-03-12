# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-02 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0031_auto_20180402_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='camp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='camps.Camp'),
        ),
    ]
