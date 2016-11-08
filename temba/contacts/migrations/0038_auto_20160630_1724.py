# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0037_auto_20160630_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='channel',
            new_name='channels',
        ),
    ]
