# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0003_auto_20141210_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta_Inco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Respuesta_Incorrecta', models.CharField(max_length=500)),
                ('pregunta', models.ForeignKey(to='preguntas.Pregunta')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
