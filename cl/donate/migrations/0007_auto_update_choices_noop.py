# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-24 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0006_add_unlimited_alert_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='status',
            field=models.SmallIntegerField(choices=[(0, b'Awaiting Payment'), (1, b'Unknown Error'), (2, b'Completed, but awaiting processing'), (3, b'Cancelled'), (4, b'Processed'), (5, b'Pending'), (6, b'Failed'), (7, b'Reclaimed/Refunded'), (8, b'Captured'), (9, b'Disputed'), (10, b'Dispute closed')]),
        ),
    ]
