# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 17:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_auto_20171101_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceitems',
            name='title',
            field=models.ForeignKey(default='Название услуги', on_delete=django.db.models.deletion.CASCADE, to='auto.TypeOfWorks', verbose_name='Название'),
        ),
    ]