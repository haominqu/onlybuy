# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-17 03:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.IntegerField(choices=[(0, '未绑定'), (1, '工商银行'), (2, '建设银行'), (3, '中信银行'), (4, '中国银行'), (5, '支付宝')], default=0, verbose_name='绑定银行')),
                ('bankid', models.CharField(max_length=13, verbose_name='银行卡号')),
                ('status', models.BooleanField(default=False, verbose_name='是否冻结')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]