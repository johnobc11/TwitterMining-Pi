# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Htweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.TextField()),
                ('tweet_date', models.DateTimeField()),
                ('tweet_favour_count', models.CharField(max_length=200)),
                ('tweet_recount', models.CharField(max_length=200)),
                ('tweet_text', models.TextField()),
            ],
        ),
    ]
