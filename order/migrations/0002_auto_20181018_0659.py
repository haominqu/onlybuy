# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-18 06:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordergoods',
            name='trprice',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='商品实际'),
        ),
    ]
