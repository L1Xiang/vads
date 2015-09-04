# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vads', '0003_auto_20150727_0504'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='second_name',
            new_name='last_name',
        ),
    ]
