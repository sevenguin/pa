# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-28 15:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pa_message', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t_questions',
            old_name='question_title',
            new_name='question_info',
        ),
    ]
