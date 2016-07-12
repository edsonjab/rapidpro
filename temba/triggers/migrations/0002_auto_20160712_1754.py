# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0031_auto_20160414_0642'),
        ('flows', '0053_auto_20160414_0642'),
        ('triggers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TriggerToFlow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channels', models.ManyToManyField(to='channels.Channel', blank=True)),
                ('flow', models.ForeignKey(blank=True, to='flows.Flow', null=True)),
                ('trigger', models.ForeignKey(to='triggers.Trigger')),
            ],
        ),
        migrations.AddField(
            model_name='trigger',
            name='flows',
            field=models.ManyToManyField(help_text='Which flow will be started', to='flows.Flow', verbose_name='Flow', through='triggers.TriggerToFlow', blank=True),
        ),
    ]
