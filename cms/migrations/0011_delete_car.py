# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-17 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_car'),
    ]

    operations = [
        migrations.DeleteModel(
            name='car',
        ),
    ]