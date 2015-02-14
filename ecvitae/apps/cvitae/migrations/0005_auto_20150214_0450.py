# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvitae', '0004_auto_20150214_0436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education',
            name='author',
        ),
        migrations.RemoveField(
            model_name='job',
            name='author',
        ),
    ]
