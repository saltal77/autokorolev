# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0010_adress_steet'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adress',
            old_name='steet',
            new_name='street',
        ),
    ]
