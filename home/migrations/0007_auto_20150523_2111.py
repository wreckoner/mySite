# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150523_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeinformation',
            name='start',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homeinformation',
            name='stop',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='homeinformation',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
