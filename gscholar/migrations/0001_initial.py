# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('email_domain', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('timestamp', models.DateField(auto_now=True)),
                ('coauthors', models.ManyToManyField(related_name='coauthors_rel_+', to='gscholar.User')),
                ('organization', models.ForeignKey(to='gscholar.Organization')),
            ],
        ),
    ]
