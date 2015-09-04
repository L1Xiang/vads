# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vads', '0004_auto_20150727_0636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='id',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_type',
            field=models.IntegerField(null=True, max_length=1, choices=[(0, 'Poster'), (1, 'ScreenOwner')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(primary_key=True, related_name='user_profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
