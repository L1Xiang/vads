# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vads', '0010_adlist_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adlist',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
