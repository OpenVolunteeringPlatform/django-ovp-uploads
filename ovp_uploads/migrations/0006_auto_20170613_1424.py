# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-13 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ovp_uploads', '0005_auto_20170522_2006'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagegalery',
            options={'verbose_name': 'image gallery', 'verbose_name_plural': 'image galleries'},
        ),
    ]