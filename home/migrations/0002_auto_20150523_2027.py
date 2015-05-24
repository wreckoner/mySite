# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagedata',
            name='category',
            field=models.CharField(default=b'WR', max_length=2, choices=[(b'PR', b'Projects and Research'), (b'ED', b'Education'), (b'WR', b'Work')]),
        ),
    ]
