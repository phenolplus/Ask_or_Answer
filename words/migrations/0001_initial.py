# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500, blank=True)),
                ('answered', models.BooleanField(default=False)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
