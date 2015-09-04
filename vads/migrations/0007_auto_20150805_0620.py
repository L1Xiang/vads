# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vads', '0006_auto_20150805_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='info',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='ad_type',
            field=models.IntegerField(choices=[(1, 'Picture'), (2, 'video')], null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.IntegerField(choices=[(0, 'Poster'), (1, 'ScreenOwner')], null=True),
        ),
    ]
