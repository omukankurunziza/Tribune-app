# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-22 14:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20190322_1546'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='editor',
            new_name='user',
        ),
    ]
