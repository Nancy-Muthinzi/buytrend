# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0004_auto_20190319_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
