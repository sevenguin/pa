# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-09 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_user',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('lasttime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
