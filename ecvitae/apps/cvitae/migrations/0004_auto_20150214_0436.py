# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvitae', '0003_auto_20150213_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
                ('descr', models.TextField(blank=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('author', models.ForeignKey(to='cvitae.Author')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('loc', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show', models.BooleanField(default=True)),
                ('cv', models.ForeignKey(to='cvitae.CV')),
                ('edu', models.ForeignKey(to='cvitae.Education')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('show', models.BooleanField(default=True)),
                ('cv', models.ForeignKey(to='cvitae.CV')),
                ('job', models.ForeignKey(to='cvitae.Job')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='education',
            name='institution',
            field=models.ForeignKey(to='cvitae.Institution'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cv',
            name='aboutme',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cv',
            name='edus',
            field=models.ManyToManyField(to='cvitae.Education', through='cvitae.Study'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cv',
            name='jobs',
            field=models.ManyToManyField(to='cvitae.Job', through='cvitae.Work'),
            preserve_default=True,
        ),
    ]
