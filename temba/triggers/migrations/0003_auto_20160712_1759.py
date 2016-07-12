# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from temba.triggers.models import TriggerToFlow

def make_many_flows(app, schema_editor):
    from django.apps import apps
    trigger_list = apps.get_model('triggers', 'Trigger')

    for t in trigger_list.objects.all():
        TriggerToFlow.objects.create(trigger = t, flow =t.flow )

class Migration(migrations.Migration):

    dependencies = [
        ('triggers', '0002_auto_20160712_1754'),
    ]

    operations = [
        migrations.RunPython(make_many_flows),
    ]
