# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0006_auto_20160721_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='genre',
        ),
        migrations.AddField(
            model_name='albumartist',
            name='genre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='song.Genre'),
            preserve_default=False,
        ),
    ]
