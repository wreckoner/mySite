# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_homeinformation_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeinformation',
            name='url',
            field=models.URLField(default=b'', blank=True),
        ),
    ]
