# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from temba.triggers.models import TriggerToFlow
from temba.channels.models import Channel
def make_many_flows(app, schema_editor):
    from django.apps import apps
    trigger_list = apps.get_model('triggers', 'Trigger')

    for t in trigger_list.objects.all():
        trigger_to_flow = TriggerToFlow.objects.create(trigger = t, flow =t.flow)
        channels = Channel.objects.filter(org = t.org)
        for channel in channels:
            trigger_to_flow.channels.add(channel)

class Migration(migrations.Migration):

    dependencies = [
        ('triggers', '0002_auto_20160712_1754'),
    ]

    operations = [
        migrations.RunPython(make_many_flows),
    ]
