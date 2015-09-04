# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vads', '0012_auto_20150806_0700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(max_length=10, choices=[('poster', 'Poster'), ('owner', 'ScreenOwner')], null=True),
        ),
    ]
