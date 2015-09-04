# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vads', '0005_auto_20150802_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ad_type', models.IntegerField(choices=[(1, 'Picture'), (2, 'video')], max_length=1, null=True)),
                ('slug', models.SlugField(max_length=255)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='users')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='ad',
            unique_together=set([('user', 'name')]),
        ),
    ]
