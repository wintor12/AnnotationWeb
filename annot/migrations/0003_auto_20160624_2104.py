# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annot', '0002_story_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
