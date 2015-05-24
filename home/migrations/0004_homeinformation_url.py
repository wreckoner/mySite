# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150523_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeinformation',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
