# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataSlice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capture_time', models.DateTimeField(auto_now_add=True, unique=True)),
                ('curr_room_temp', models.DecimalField(max_digits=3, decimal_places=1)),
                ('curr_room_humid', models.DecimalField(max_digits=3, decimal_places=1)),
                ('local_outside_icon', models.CharField(max_length=30)),
                ('local_outside_temp', models.DecimalField(max_digits=3, decimal_places=1)),
                ('local_outside_humid', models.DecimalField(max_digits=3, decimal_places=1)),
                ('local_outside_apparent_temp', models.DecimalField(max_digits=3, decimal_places=1)),
            ],
        ),
    ]
