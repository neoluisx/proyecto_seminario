# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0005_respuesta_inco_tema'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta_inco',
            name='tema',
        ),
    ]
