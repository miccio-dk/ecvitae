# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvitae', '0005_auto_20150214_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='title',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='job',
            name='position',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
