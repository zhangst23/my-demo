# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-28 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yanji', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='yanji',
            name='status',
            field=models.CharField(choices=[('d', '\u8349\u7a3f'), ('p', '\u53d1\u8868')], default='p', max_length=1, verbose_name='\u6587\u7ae0\u72b6\u6001'),
        ),
    ]