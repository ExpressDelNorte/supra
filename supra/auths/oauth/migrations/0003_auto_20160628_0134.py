# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 06:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oauth', '0002_auto_20160628_0055'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OAthToken',
            new_name='OAuthToken',
        ),
    ]
