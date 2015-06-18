# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0002_twittertrend'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterAvailableWoeid',
            fields=[
                ('woeid', models.IntegerField(serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
