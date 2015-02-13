# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvitae', '0002_auto_20150213_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='address',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='author',
            name='birthday',
            field=models.DateField(blank=True),
            preserve_default=True,
        ),
    ]
