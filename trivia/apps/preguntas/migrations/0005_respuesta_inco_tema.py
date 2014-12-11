# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0004_respuesta_inco'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuesta_inco',
            name='tema',
            field=models.ForeignKey(default=34, to='preguntas.Tema'),
            preserve_default=False,
        ),
    ]
