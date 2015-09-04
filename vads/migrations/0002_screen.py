# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('user', models.ForeignKey(related_name='screens', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
