# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta',
            name='respusta_opcional1',
            field=models.CharField(default=12, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respuesta',
            name='respusta_opcional2',
            field=models.CharField(default=343, max_length=500),
            preserve_default=False,
        ),
    ]
