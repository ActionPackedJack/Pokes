# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-24 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_user_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='folks_poked',
            field=models.ManyToManyField(related_name='_user_folks_poked_+', to='login_app.User'),
        ),
    ]