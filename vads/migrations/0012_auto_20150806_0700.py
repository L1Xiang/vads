# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vads', '0011_auto_20150806_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='ad_type',
            field=models.CharField(null=True, max_length=10, choices=[('picture', 'Picture'), ('video', 'Video')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.IntegerField(null=True, choices=[('poster', 'Poster'), ('owner', 'ScreenOwner')]),
        ),
    ]
