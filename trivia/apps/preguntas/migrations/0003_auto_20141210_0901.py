# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0002_auto_20141203_0426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta',
            name='respusta_opcional',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='respusta_opcional1',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='respusta_opcional2',
        ),
    ]
