# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trends', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterTrend',
            fields=[
                ('location_id', models.IntegerField(serialize=False, primary_key=True)),
                ('trends', models.TextField()),
                ('location', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
