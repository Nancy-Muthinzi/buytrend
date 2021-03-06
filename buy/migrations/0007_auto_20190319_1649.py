# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0006_auto_20190319_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('description', models.TextField(max_length=250)),
            ],
            options={
                'ordering': ['image'],
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='buy.Category'),
        ),
    ]
