# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-29 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('loc_label', models.CharField(blank=True, max_length=150, null=True)),
                ('latitude', models.DecimalField(decimal_places=10, default=0, max_digits=20)),
                ('Longitude', models.DecimalField(decimal_places=10, default=0, max_digits=20)),
                ('ip', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]