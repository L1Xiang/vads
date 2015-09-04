# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vads', '0009_auto_20150806_0445'),
    ]

    operations = [
        migrations.AddField(
            model_name='adlist',
            name='info',
            field=models.TextField(null=True, max_length=1000),
        ),
    ]
