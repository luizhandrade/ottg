# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_test'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
    ]
