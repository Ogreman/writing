# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-22 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writing', '0005_auto_20160521_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]