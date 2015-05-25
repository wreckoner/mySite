# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterToken',
            fields=[
                ('consumerKey', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('consumerSecret', models.CharField(max_length=100)),
                ('accessToken', models.CharField(max_length=100)),
                ('accessTokenSecret', models.CharField(max_length=100)),
            ],
        ),
    ]
