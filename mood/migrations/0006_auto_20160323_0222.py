# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 02:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0005_auto_20160323_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='anger',
            new_name='anger_level',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='fear',
            new_name='anxiety_level',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='happiness',
            new_name='happiness_level',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='sadness',
            new_name='motivation_level',
        ),
    ]
