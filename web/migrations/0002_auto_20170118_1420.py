# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
    ]