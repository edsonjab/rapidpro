# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0031_auto_20160414_0642'),
        ('contacts', '0036_contact_channel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='channel',
        ),
        migrations.AddField(
            model_name='contact',
            name='channel',
            field=models.ManyToManyField(help_text='The channlen that this contact will use', related_name='channel_contacts', verbose_name='Channel', to='channels.Channel', blank=True),
        ),
    ]
