# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 07:18
from __future__ import absolute_import, division, print_function, unicode_literals

import gc

from array import array
from django.db import connection, migrations
from temba.utils import chunk_list


def populate_flowrun_uuid(FlowRun):
    with connection.cursor() as c:
        c.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')

    run_ids = array(str('l'), FlowRun.objects.filter(uuid=None).values_list('id', flat=True))
    if not run_ids:
        return

    gc.collect()

    print("Fetched %d flow run ids that need UUIDs..." % len(run_ids))
    num_updated = 0

    with connection.cursor() as c:
        for id_batch in chunk_list(run_ids, 1000):
            c.execute('UPDATE flows_flowrun SET uuid = uuid_generate_v4() WHERE id IN (%s)' % ','.join([str(f) for f in id_batch]))

            num_updated += len(id_batch)
            print(" > Updated %d of %d flow runs" % (num_updated, len(run_ids)))


def apply_manual():
    from temba.flows.models import FlowRun
    populate_flowrun_uuid(FlowRun)


def apply_as_migration(apps, schema_editor):
    FlowRun = apps.get_model('flows', 'FlowRun')
    populate_flowrun_uuid(FlowRun)


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0107_flowrun_uuid'),
    ]

    operations = [
        migrations.RunPython(apply_as_migration)
    ]
