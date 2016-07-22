# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0005_auto_20160720_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='value',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='artist',
            old_name='value',
            new_name='artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='album_artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='song',
            name='year',
        ),
        migrations.AddField(
            model_name='album',
            name='album_artist',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='song.AlbumArtist'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='year',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='song.Year'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='song.Genre'),
            preserve_default=False,
        ),
    ]