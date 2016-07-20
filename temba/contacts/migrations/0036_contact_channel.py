# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0031_auto_20160414_0642'),
        ('contacts', '0035_auto_20160414_0642'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='channel',
            field=models.ForeignKey(related_name='channel_contacts', blank=True, to='channels.Channel', help_text='The channlen that this contact will use', null=True, verbose_name='Channel'),
        ),
    ]
