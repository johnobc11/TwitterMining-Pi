# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 09:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Hermtweets', '0004_auto_20170410_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hermtweets',
            name='tweet_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 9, 53, 22, 772226, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hermtweets',
            name='tweet_timestamp',
            field=models.TimeField(default=datetime.datetime(2017, 4, 10, 9, 53, 22, 772822, tzinfo=utc)),
        ),
    ]
