# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 10:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('memberapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='memberapp.GoodsType'),
            preserve_default=False,
        ),
    ]
