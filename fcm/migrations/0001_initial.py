# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_id', models.CharField(max_length=50, unique=True, verbose_name='Device ID')),
                ('dev_type', models.CharField(choices=[('IOS', 'iOS'), ('ANDROID', 'Android')], default='Android', max_length=255, verbose_name='Device Type')),
                ('reg_id', models.CharField(max_length=255, unique=True, verbose_name='Registration ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Modified date')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'Devices',
                'ordering': ['-modified_date'],
                'verbose_name': 'Device',
            },
        ),
    ]