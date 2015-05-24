# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(unique=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(default=b'WR', max_length=2, choices=[(b'PR', b'Projects and Researchs'), (b'ED', b'Education'), (b'WR', b'Work')])),
            ],
        ),
    ]
