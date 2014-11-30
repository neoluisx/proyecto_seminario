# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import trivia.apps.usuario.thumbs


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='usuario',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='correo',
        ),
        migrations.AddField(
            model_name='perfil',
            name='avatar',
            field=trivia.apps.usuario.thumbs.ImageWithThumbsField(default=1, upload_to=b'img_user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='pais',
            field=models.CharField(default=12, max_length=b'30'),
            preserve_default=False,
        ),
    ]
