# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 07:24
from __future__ import absolute_import, division, print_function, unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    INDEX_SQL = """
CREATE INDEX msgs_msg_external_id_where_nonnull
ON msgs_msg(external_id)
WHERE external_id IS NOT NULL;
    """

    dependencies = [
        ('msgs', '0076_install_triggers'),
    ]

    operations = [
        migrations.RunSQL(INDEX_SQL)
    ]
