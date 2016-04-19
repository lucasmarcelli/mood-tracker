# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mood', '0019_auto_20160410_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('track_daily', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('attribute_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mood.Attribute')),
                ('name', models.CharField(max_length=75)),
            ],
            bases=('mood.attribute',),
        ),
        migrations.CreateModel(
            name='Dietary',
            fields=[
                ('consumable_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mood.Consumable')),
                ('calories', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            bases=('mood.consumable',),
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('dietary_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mood.Dietary')),
                ('volume', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            bases=('mood.dietary',),
        ),
    ]
