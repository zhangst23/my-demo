# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-29 09:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yanji', '0008_auto_20171029_1700'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Scripttype',
            new_name='Dramatype',
        ),
        migrations.RenameField(
            model_name='drama',
            old_name='scripttype',
            new_name='dramatype',
        ),
    ]
