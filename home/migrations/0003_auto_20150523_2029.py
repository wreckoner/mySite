# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150523_2027'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePageData',
            new_name='HomeInformation',
        ),
    ]
