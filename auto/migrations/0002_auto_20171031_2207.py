# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interest',
            options={'verbose_name': 'Блок Важно Знать'},
        ),
        migrations.AlterField(
            model_name='interest',
            name='text',
            field=models.TextField(verbose_name='Блок Важно знать Текст'),
        ),
    ]
