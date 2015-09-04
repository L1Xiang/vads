# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vads', '0014_auto_20150806_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='ads'),
        ),
    ]
