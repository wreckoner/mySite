# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20150523_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeinformation',
            name='start',
            field=models.DateField(default=datetime.datetime(2015, 5, 24, 0, 54, 56, 574000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeinformation',
            name='stop',
            field=models.DateField(default=datetime.datetime(2015, 5, 24, 0, 55, 12, 393000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
