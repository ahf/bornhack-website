# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0044_coinifyapiinvoice_coinify_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coinifyapicallback',
            old_name='valid',
            new_name='authenticated',
        ),
    ]