# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gscholar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='title',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
