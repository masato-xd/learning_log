# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-26 09:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_auto_20161226_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='owner',
        ),
    ]
