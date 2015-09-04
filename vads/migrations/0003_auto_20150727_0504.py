# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vads', '0002_screen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='user_profile'),
        ),
        migrations.AlterUniqueTogether(
            name='screen',
            unique_together=set([('user', 'name')]),
        ),
    ]
