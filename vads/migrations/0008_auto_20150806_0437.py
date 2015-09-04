# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vads', '0007_auto_20150805_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdList',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, blank=True)),
                ('user', models.ForeignKey(related_name='ad_list', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='adlist',
            unique_together=set([('user', 'name')]),
        ),
    ]
