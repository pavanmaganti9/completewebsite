# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='website',
            options={'verbose_name_plural': 'Contents'},
        ),
    ]
