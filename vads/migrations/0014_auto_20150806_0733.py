# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vads', '0013_auto_20150806_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='ad_list',
            field=models.ForeignKey(related_name='ads', to='vads.AdList', null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='user',
            field=models.ForeignKey(related_name='ads', to=settings.AUTH_USER_MODEL),
        ),
    ]
