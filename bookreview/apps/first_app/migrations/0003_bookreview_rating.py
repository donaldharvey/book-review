# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 16:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20161212_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='rating',
            field=models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
