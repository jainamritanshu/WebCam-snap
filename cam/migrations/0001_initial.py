# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-27 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=1000)),
                ('snap_link', models.CharField(max_length=1000)),
            ],
        ),
    ]
